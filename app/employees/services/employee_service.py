from app.employees.repositories import EmployeeRepository
from app.db.database import SessionLocal
from app.employees.exceptions import *
import hashlib


class EmployeeServices:

    @staticmethod
    def create_employee(name, surname, email, phone_number, position):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                if email in employee_repository.get_employees_emails():
                    raise EmployeeEmailException(status_code=400,
                                                 detail=f"Employee with provided email - {email} already exists.")
                if phone_number in employee_repository.get_employees_phone_numbers():
                    raise EmployeePhoneNumberException(status_code=400,
                                                       detail=f"Employee with provided phone number"
                                                              f" - {phone_number} already exists.")
                return employee_repository.create_employee(name, surname, email, phone_number, position)
        except Exception as e:
            raise e

    @staticmethod
    def create_employee_with_password(name, surname, email, phone_number, position, password):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                if email in employee_repository.get_employees_emails():
                    raise EmployeeEmailException(status_code=400,
                                                 detail=f"Employee with provided email - {email} already exists.")
                if phone_number in employee_repository.get_employees_phone_numbers():
                    raise EmployeePhoneNumberException(status_code=400,
                                                       detail=f"Employee with provided phone number"
                                                              f" - {phone_number} already exists.")
                return employee_repository.create_employee_with_password(name, surname, email, phone_number, position,
                                                                         password)
        except Exception as e:
            raise e

    @staticmethod
    def get_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_employee_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_employees():
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_all_employees()
        except Exception as e:
            raise e

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.delete_employee_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_employee_is_admin(employee_id: str, is_admin: bool):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.update_employee_is_admin(employee_id, is_admin)
        except Exception as e:
            raise e

    @staticmethod
    def login_employee(email: str, password: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee = employee_repository.get_employee_by_email(email)
                if password != employee.password:
                    raise EmployeeInvalidPassword(status_code=401,
                                                  detail="Invalid password")
                return employee
        except Exception as e:
            raise e
