from app.employees.services import EmployeeServices, signJWT
from fastapi import HTTPException, Response
from app.employees.exceptions import *


class EmployeeController:

    @staticmethod
    def create_employee(name: str, surname: str, email: str, phone_number: str, position: str):
        try:
            employee = EmployeeServices.create_employee(name, surname, email, phone_number, position)
            return employee
        except EmployeeEmailException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except EmployeePhoneNumberException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_employee_with_password(name: str, surname: str, email: str, phone_number: str, position: str, password: str):
        try:
            employee = EmployeeServices.create_employee_with_password(name, surname, email, phone_number, position, password)
            return employee
        except EmployeeEmailException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except EmployeePhoneNumberException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_by_id(employee_id: str):
        employee = EmployeeServices.get_employee_by_id(employee_id)
        if employee:
            return employee
        else:
            raise HTTPException(status_code=400, detail=f"Employee with provided id: {employee_id} does not exist")

    @staticmethod
    def get_all_employees():
        employees = EmployeeServices.get_all_employees()
        return employees

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        employee = EmployeeServices.get_employee_by_id(employee_id)
        if employee:
            EmployeeServices.delete_employee_by_id(employee_id)
            return Response(content=f"Employee with id - {employee_id} is deleted")
        else:
            raise HTTPException(status_code=400, detail=f"Employee with provided id: {employee_id} does not exist")

    @staticmethod
    def update_employee_is_admin(employee_id: str, is_admin: bool):
        employee = EmployeeServices.get_employee_by_id(employee_id)
        if employee:
            return EmployeeServices.update_employee_is_admin(employee_id, is_admin)
        else:
            raise HTTPException(status_code=400, detail=f"Employee with provided id: {employee_id} does not exist")

    @staticmethod
    def login_employee(email: str, password: str):
        try:
            employee = EmployeeServices.login_employee(email, password)
            if employee.is_admin:
                return signJWT(employee.id, "admin")
            return signJWT(employee.id, "not admin")
        except EmployeeInvalidPassword as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
