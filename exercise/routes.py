
import logging
from flask import request, render_template
from flask_api import status
from flask_restplus import Api, Resource, fields, reqparse

from . import app, pool

from exercise.device import Device
from exercise.pool import DevicePool
from exercise.errors import ErrorDeviceAlreadyExists, ErrorDeviceNotFound, ErrorInvalidData

####################################################################################################
# Configure Swagger
####################################################################################################
api = Api(app,
          version='1.0.0',
          title="Pasqal REST API Service",
          description="This is a device and job scheduler",
          default="pasqal",
          default_label="Pasqal",
          doc='/apidocs',
          prefix='/api'
         )

# model to expect in device API calls
device_model = api.model('Device', {
    "id": fields.String(readOnly=True,
            description='The unique id assigned to a Device (QPU)\n'),
    "address": fields.String(readOnly=True,
            description='Physical/ IP Address of the device\n'),
    "type": fields.String(required=True,
            description='The type of device\n'),
    "size": fields.Integer(required=True,
            description='Size (in bytes)\n')
})

# model to expect in device API calls
job_model = api.model('Job', {
    "id": fields.String(readOnly=True,
            description='The unique id assigned to a Job\n'),
    "priority": fields.Integer(required=True,
            description='Priority\n'),
    "type": fields.String(required=True,
            description='The type of device\n'),
    "user_id": fields.String(readOnly=True,
            description='ID of the User\n'),
    "program_id": fields.String(readOnly=True,
            description='ID of the Program\n')
})

####################################################################################################
# INDEX
####################################################################################################
@app.route("/")
def index():
    """ Root URL response """
    app.logger.info("Request for Root URL")
    return app.send_static_file('index.html')
    # return render_template('index.html')

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
            app.logger.info("Request to add the device {} to the pool.".format(api.payload["id"]))
            device = Device(api.payload["id"], api.payload["address"], api.payload["type"], api.payload["size"])
            pool.add(device)
            app.logger.info("Request to add the device {} to the pool.".format(api.payload["id"]))
            return device.serialize(), status.HTTP_201_CREATED
        except ErrorDeviceAlreadyExists as err:
            api.abort(status.HTTP_409_CONFLICT, err)
        except Exception as err:
            api.abort(status.HTTP_400_BAD_REQUEST, err)


#  PATH: /device/device_id
@api.route('/device/<str:device_id>')
@api.param('device_id', 'The Inventory identifiers')
class DeviceResource(Resource):
    """
    DELETE /device - This will let us REMOVE a device to the pool.
    """
    #------------------------------------------------------------------
    # REMOVE A DEVICE FROM THE POOL
    #------------------------------------------------------------------
    @api.doc('delete_device')
    @api.response(status.HTTP_204_NO_CONTENT, 'Inventory deleted')
    def delete(self, product_id, condition):
        """
        DELETE /device - This will let us REMOVE a device to the pool.
        """
        try:
            app.logger.info("Request to remove device {} from the pool".format(device_id))
            pool.remove(device_id)
            app.logger.info("Device {} successfully removed from the pool".format(device_id))
            return '', status.HTTP_204_NO_CONTENT
        except ErrorInvalidData as err:
            api.abort(status.HTTP_400_BAD_REQUEST, err)


####################################################################################################
# Job
####################################################################################################
#  PATH: /job
# @api.route('/job', strict_slashes=False)
# class JobBase(Resource):
#     """
#     POST    /job - This will let us ADD a job to the queue.
#     """
#     #------------------------------------------------------------------
#     # ADD A NEW JOB TO THE QUEUE
#     #------------------------------------------------------------------
#     @api.doc('create_job')
#     @api.expect(job_model)
#     @api.response(status.HTTP_400_BAD_REQUEST, 'The posted data was not valid')
#     @api.response(status.HTTP_201_CREATED, 'Job added successfully to the queue')
#     @api.marshal_with(job_model, code=status.HTTP_201_CREATED)
#     # @token_required
#     def post(self):
#         """
#         Creates a Inventory
#         This endpoint will create a Inventory based the data in the body that is posted
#         """
#         try:
#             app.logger.info("Request to create an Inventory record")
#             inventory = Inventory()
#             inventory.deserialize(api.payload)
#             inventory.validate_data()
#
#             if Inventory.find_by_product_id_condition(api.payload[keys.KEY_PID], api.payload[keys.KEY_CND]):
#                 api.abort(status.HTTP_409_CONFLICT,
#                         "Inventory with ({}, {})".format(inventory.product_id, inventory.condition))
#
#             inventory.create()
#             location_url = api.url_for(InventoryResource, product_id=inventory.product_id,
#                 condition=inventory.condition, _external=True)
#             app.logger.info("Inventory ({}, {}) created."\
#                             .format(inventory.product_id, inventory.condition))
#             return inventory.serialize(), status.HTTP_201_CREATED, {'Location': location_url}
#         except DataValidationError as err:
#             api.abort(status.HTTP_400_BAD_REQUEST, err)
