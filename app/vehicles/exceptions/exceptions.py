class VehicleLicensePlateException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class InvalidCustomerIdException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
