import os
import sys
import logging
import threading

from flask import Flask
from exercise.queue import ProcessQueue
from exercise.pool import DevicePool

# Create Flask application
app = Flask(__name__)
app.config.from_object("config")
app.config['LOGGING_LEVEL'] = logging.INFO
app.logger.info("Scheduler inititalized!")

# Create queue object
queue = ProcessQueue()

# Create pool object
device_pool = DevicePool()

# if __name__ == '__main__':
    # print('hello')
    # from exercise.worker import Worker
    # pass
    # Running the API calls asynchronously
    # api = API()
    # threading.Thread(target=api.run)

    # TODO:
    # worker = Worker()
    # worker.run()
    # app.run()
