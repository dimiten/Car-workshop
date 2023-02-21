"""Customer exceptions"""


class CustomerEmailException(Exception):
    """Exception if customer is created with an already existing email"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class CustomerPhoneNumberException(Exception):
    """Exception if customer is created with an already existing phone number"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
