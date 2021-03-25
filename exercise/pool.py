
from exercise.errors import ErrorDeviceAlreadyExists, ErrorDeviceNotFound, ErrorInvalidData
from exercise.device import Device
from typing import Dict

class DevicePool():

    # common devices' pool
    devices: Dict[str, Device]

    def add(self, device: Device):
        """
        Adds a device to the pool
        :type device: Device
        :rtype: None
        """
        if device.id in self.devices:
            raise ErrorDeviceAlreadyExists("Device {} already exists".format(device.id)))
        self.devices[device.id] = device

    def remove(self, device_id: str):
        """
        Removes a device from the pool
        :type device_id: str
        :rtype: None
        """
        if not device_id:
            raise ErrorInvalidData("Invalid device_id {}".format(device_id))
        if device_id in self.devices:
            del self.devices[device_id]

    def list(self):
        """
        Returns a list of IDs of devices in the pool
        :rtype: List[int]
        """
        # return [d for d in self.devices.values()]
        return list(self.devices.keys())
