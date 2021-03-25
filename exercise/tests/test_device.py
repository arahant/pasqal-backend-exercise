
from exercise.device import Device

def test_device():
    device1 = Device(12, "addr1", "type1", 21)
    assert device1.id == 12

    device2 = Device(22, "addr2", "type2", 21)
    assert device2.id == 22

    device3 = Device(121, "addr3", "type3", 32)
    assert device3.id == 121
