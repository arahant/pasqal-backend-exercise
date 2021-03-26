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

    """
    A device (QPU) can have multiple properties such as
    Quantum computing capacity, fidelity, systemic noise level, etc.
    """

    device_calls = defaultdict(int)

    def __init__(self, did, addr, type, size):
        """
        :type did: str
        :type addr: str
        :type type: str
        :type size: int
        :rtype: None
        """
        self.id = did
        self.address = addr
        self.type = type
        self.size = size

    def serialize(self):
        """ Serializes a Device into a dictionary """
        return {
            "id": self.id,
            "address": self.address,
            "type": self.type,
            "size": self.size,
            "state": self.state
        }

    def send(self, instructions):
        """
        This method sends quantum computing instructions to the device.
        """
        Device.call_device(self.id)
        return random.getrandbits(self.size)


    @classmethod
    def call_device(cls, id):
        """
        The following code is here to mock calls to the devices
        We register calls to each device and we respond random bitstrings
        """
        cls.device_calls[id] += 1
        time.sleep(2 * cls.device_calls[id])
        cls.device_calls[id] -= 1
