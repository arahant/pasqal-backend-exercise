import time
import random
from dataclasses import dataclass
from enum import Enum
from collections import defaultdict


class DeviceState(Enum):
    UP = 'UP'


@dataclass
class Device():

    id: str
    address: str
    type: str
    size: int
    state: DeviceState = None

    def send(self, instructions):
        call_device(self.id)
        return random.getrandbits(self.size)


# The following code is here to mock calls to the devices
# We register calls to each device and we respond random bitstrings

device_calls = defaultdict(int)


def call_device(id):
    device_calls[id] += 1
    time.sleep(2 * device_calls[id])
    device_calls[id] -= 1
