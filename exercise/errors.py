
class Error(Exception):
    pass

class ErrorDeviceAlreadyExists(Error):
    pass

class ErrorDeviceNotFound(Error):
    pass

class ErrorEmptyQueue(Error):
    pass

class ErrorInvalidData(Error):
    pass
