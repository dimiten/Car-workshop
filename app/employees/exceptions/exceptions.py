class EmployeeEmailException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class EmployeePhoneNumberException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class EmployeeInvalidPassword(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
