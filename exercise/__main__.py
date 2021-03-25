
import os
import sys
import logging
import threading
from flask import Flask

from exercise.queue import PriorityQueue
from exercise.api import API
from exercise import utils
from exercise.pool import DevicePool
from exercise.job import Job
from exercise.worker import Worker

# Create Flask application
app = Flask(__name__)

app.config.from_object("config")
app.config['LOGGING_LEVEL'] = logging.INFO
app.logger.info("Scheduler inititalized!")

queue = PriorityQueue()
pool = DevicePool()

if __name__ == '__main__':
    # Running the API calls asynchronously
    # api = API()
    # threading.Thread(target=api.run)

    # TODO:
    # worker = Worker()
    # worker.run()
