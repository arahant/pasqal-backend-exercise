class Error(Exception):
    pass


class ErrorDeviceAlreadyExists(Error):
    pass


class ErrorDeviceNotFound(Error):
    pass
