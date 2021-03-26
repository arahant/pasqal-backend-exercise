
import pytest
from exercise.device import Device
from exercise.pool import DevicePool
from exercise.errors import ErrorDeviceAlreadyExists, ErrorInvalidData

pool = DevicePool()

def test_pool_add():
    device1 = Device("12", "addr1", "type1", 21)
    pool.add(device1)
    assert pool.search("12")
    pytest.raises(ErrorDeviceAlreadyExists, pool.add, device1)

    device2 = Device("22", "addr2", "type2", 21)
    pool.add(device2)
    assert pool.search("22")

    device3 = Device("121", "addr3", "type3", 32)
    pool.add(device3)
    assert pool.search("121")

def test_pool_remove():
    pool.remove("12")
    assert not pool.search("12")

    pytest.raises(ErrorInvalidData, pool.remove, None)

    pool.remove("121")
    assert not pool.search("121")

def test_pool_list():
    devices = pool.list()
    assert len(devices) == 1
