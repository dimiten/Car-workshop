"""Vehicle service exceptions"""


class InvalidVehicleException(Exception):
    """Invalid vehicle exception"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class InvalidEmployeeException(Exception):
    """Invalid employee exception"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class InvalidServiceTypeException(Exception):
    """Invalid service type exception"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class InvalidDateTypeException(Exception):
    """Invalid date type exception"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
