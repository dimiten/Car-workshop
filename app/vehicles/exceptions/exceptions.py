"""Vehicle exceptions"""


class VehicleLicensePlateException(Exception):
    """Vehicle license plate exception"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class InvalidCustomerIdException(Exception):
    """Invalid customer id exception"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
