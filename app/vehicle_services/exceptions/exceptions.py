class InvalidVehicleException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class InvalidEmployeeException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class InvalidServiceTypeException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
