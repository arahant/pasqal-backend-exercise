
from exercise.errors import ErrorDeviceAlreadyExists, ErrorDeviceNotFound
from exercise.device import Device
from typing import Dict


class DevicePool():
    devices: Dict[str, Device]

    def __init__(self):
        self.devices = {}

    def add(self, device: Device):
        if device.id in self.devices:
            raise ErrorDeviceAlreadyExists
        self.devices[device.id] = device

    def remove(self, device_id: str):
        if device_id not in self.devices:
            raise ErrorDeviceNotFound
        del self.devices[device_id]

    def update(self, device: Device):
        if device.id not in self.devices:
            raise ErrorDeviceNotFound
        self.devices[device.id] = device

    def list(self):
        return [d for d in self.devices.values()]
