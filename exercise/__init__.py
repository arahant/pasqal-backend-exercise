"""
Package: app

Package for the application model and services
This module also sets up the logging to be used with gunicorn
"""

import os
import sys
import logging
from flask import Flask

from exercise.queue import PriorityQueue
from exercise.api import API
import threading

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

# Running the api should not block. You should run it asynchronously
# using threading, asyncio, or any other library you see fit.
# e.g. with threading
# api = API()
# threading.Thread(target=api.run)

# TODO:
worker = Worker()
worker.run()
