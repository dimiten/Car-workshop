"""Employee exceptions"""


class EmployeeEmailException(Exception):
    """Exception if email already exists in database"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class EmployeePhoneNumberException(Exception):
    """Exception if phone number already exists in database"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class EmployeeInvalidPassword(Exception):
    """Invalid password exception"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
