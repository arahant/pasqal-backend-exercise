import time
import random
from dataclasses import dataclass
from enum import Enum
from collections import defaultdict


class DeviceState(Enum):
    UP = 'UP'


@dataclass
class Device():

    device_id: str
    address: str
    device_type: str
    size: int
    state: DeviceState = None

    """
    A device (QPU) can have multiple properties such as
    Quantum computing capacity, fidelity, systemic noise level, etc.
    """

    device_calls = defaultdict(int)

    def __init__(self, did, addr, device_type, size):
        """
        :type did: str
        :type addr: str
        :type device_type: str
        :type size: int
        :rtype: None
        """
        self.device_id = did
        self.address = addr
        self.device_type = device_type
        self.size = size

    def serialize(self):
        """ Serializes a Device into a dictionary """
        return {
            "device_id": self.device_id,
            "address": self.address,
            "device_type": self.device_type,
            "size": self.size,
            "state": self.state
        }

    def send(self, instructions):
        """
        This method sends quantum computing instructions to the device.
        """
        Device.call_device(self.device_id)
        return random.getrandbits(self.size)


    @classmethod
    def call_device(cls, device_id):
        """
        The following code is here to mock calls to the devices
        We register calls to each device and we respond random bitstrings
        """
        cls.device_calls[device_id] += 1
        time.sleep(2 * cls.device_calls[device_id])
        cls.device_calls[device_id] -= 1
