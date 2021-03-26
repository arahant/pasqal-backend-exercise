
from flask_api import status
from flask_restplus import Api, Resource, fields

from exercise.errors import ErrorDeviceAlreadyExists, ErrorInvalidData
from exercise.device import Device
from exercise.job import Job
from exercise.main import app, device_pool, queue

####################################################################################################
# Configure Swagger
####################################################################################################
api = Api(app,doc='/swagger')

# model to expect in device API calls
device_model = api.model('Device', {
    "device_id": fields.String(readOnly=True,
            description='The unique id assigned to a Device (QPU)\n'),
    "address": fields.String(readOnly=True,
            description='Physical/ IP Address of the device\n'),
    "device_type": fields.String(required=True,
            description='The type of device\n'),
    "size": fields.Integer(required=True,
            description='Size (in bytes)\n')
})

# model to expect in device API calls
job_model = api.model('Job', {
    "job_id": fields.String(readOnly=True,
            description='The unique id assigned to a Job\n'),
    "priority": fields.Integer(required=True,
            description='Priority\n'),
    "device_type": fields.String(required=True,
            description='The type of device\n'),
    "user_id": fields.String(readOnly=True,
            description='ID of the User\n'),
    "program_id": fields.String(readOnly=True,
            description='ID of the Program\n')
})

####################################################################################################
# Device
####################################################################################################
#  PATH: /device
@api.route('/device', strict_slashes=False)
class DeviceBase(Resource):
    """
    POST /device - This will let us ADD a device to the pool.
    """
    #------------------------------------------------------------------
    # ADD A NEW DEVICE TO THE POOL
    #------------------------------------------------------------------
    @api.doc('create_device')
    @api.expect(device_model)
    @api.response(status.HTTP_400_BAD_REQUEST, 'The posted data was not valid.')
    @api.response(status.HTTP_201_CREATED, 'The device was successfully added to the pool.')
    @api.marshal_with(device_model, code=status.HTTP_201_CREATED)
    def post(self):
        """
        POST /device - This will let us ADD a device to the pool.
        """
        try:
            app.logger.info("Adding the device {} to the pool.".format(api.payload["device_id"]))
            device = Device(
                api.payload["device_id"],
                api.payload["address"],
                api.payload["device_type"],
                api.payload["size"]
            )
            device_pool.add(device)
            app.logger.info("Device {} added to the pool.".format(api.payload["device_id"]))
            return device.serialize(), status.HTTP_201_CREATED
        except ErrorDeviceAlreadyExists as err:
            api.abort(status.HTTP_409_CONFLICT, err)


#  PATH: /device/device_id
@api.route('/device/<string:device_id>')
@api.param('device_id', 'The Device identifier')
class DeviceResource(Resource):
    """
    DELETE /device - This will let us REMOVE a device to the pool.
    """
    #------------------------------------------------------------------
    # REMOVE A DEVICE FROM THE POOL
    #------------------------------------------------------------------
    @api.doc('delete_device')
    @api.response(status.HTTP_204_NO_CONTENT, 'Device removed from the pool')
    def delete(self, device_id):
        """
        DELETE /device - This will let us REMOVE a device to the pool.
        """
        try:
            app.logger.info("Request to remove device {} from the pool".format(device_id))
            device_pool.remove(device_id)
            app.logger.info("Device {} successfully removed from the pool".format(device_id))
            return '', status.HTTP_204_NO_CONTENT
        except ErrorInvalidData as err:
            api.abort(status.HTTP_400_BAD_REQUEST, err)


####################################################################################################
# Job
####################################################################################################
#  PATH: /job
@api.route('/job', strict_slashes=False)
class JobBase(Resource):
    """
    POST /job - This will let us ADD a job to the queue.
    """
    #------------------------------------------------------------------
    # ADD A NEW JOB TO THE QUEUE
    #------------------------------------------------------------------
    @api.doc('create_job')
    @api.expect(job_model)
    @api.response(status.HTTP_400_BAD_REQUEST, 'The posted data was not valid')
    @api.response(status.HTTP_201_CREATED, 'Job added successfully to the queue')
    @api.marshal_with(job_model, code=status.HTTP_201_CREATED)
    def post(self):
        """
        POST /job - This will let us ADD a job to the queue.
        """
        try:
            app.logger.info("Request to add a job into the queue")
            job = Job(
                api.payload["job_id"],
                api.payload["user_id"],
                api.payload["program_id"],
                api.payload["device_type"],
                api.payload["priority"]
            )
            queue.push(job, api.payload["priority"])
            app.logger.info("Request to add a job into the queue")
            return job.serialize(), status.HTTP_201_CREATED
        except ErrorInvalidData as err:
            api.abort(status.HTTP_400_BAD_REQUEST, err)
