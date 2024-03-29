"""Service types exceptions"""


class ServiceTypeExistsException(Exception):
    """Exception if service type with the same name already exists in database"""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
