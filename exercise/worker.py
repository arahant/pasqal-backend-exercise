
from exercise.utils import handle_result
from exercise.errors import ErrorEmptyResult
from exercise.main import device_pool, queue, app

class Worker():

    def run():
        """
        wait for new jobs on the queue and send them to the right device
        """
        try:
            job = queue.pop()
            available_devices = device_pool.list()
            device = Worker.choose_device(available_devices)
            job.result = device.send(job.instructions)
            handle_result(job)
        except ErrorEmptyResult as err:
            app.logger.info(err)

    @classmethod
    def choose_device(cls, devices):
        """
        This method chooses and returns the best fit device"""
        return devices[0]
