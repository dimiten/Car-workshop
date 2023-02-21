"""Employee repository"""


from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.employees.models import Employee


class EmployeeRepository:
    """EmployeeRepository class"""

    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, name, surname, email, phone_number, position):
        """Creates an employee"""
        try:
            employee = Employee(name, surname, email, phone_number, position)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as e:
            raise e

    def create_employee_with_password(self, name, surname, email, phone_number, position, password):
        """Creates an employee with password"""
        try:
            employee = Employee(name, surname, email, phone_number, position, password=password)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as e:
            raise e

    def get_employee_by_id(self, employee_id: str):
        """Returns an employee by id"""
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            return employee
        except Exception as e:
            raise e

    def get_all_employees(self):
        """Return all employees"""
        try:
            employees = self.db.query(Employee).all()
            return employees
        except Exception as e:
            raise e

    def delete_employee_by_id(self, employee_id: str):
        """Deletes an employee by id"""
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            self.db.delete(employee)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_employee_is_admin(self, employee_id: str, is_admin: bool):
        """Update is_admin attribute in employee"""
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            employee.is_admin = is_admin
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e

    def get_employees_emails(self):
        """Returns all emails from employees"""
        try:
            employees_emails = self.db.query(Employee.email).all()
            return [item for t in employees_emails for item in t]
        except Exception as e:
            raise e

    def get_employees_phone_numbers(self):
        """Returns all phone numbers from employees"""
        try:
            employees_phone_numbers = self.db.query(Employee.phone_number).all()
            return [item for t in employees_phone_numbers for item in t]
        except Exception as e:
            raise e

    def get_employee_by_email(self, email: str):
        """Returns an employee by email"""
        employee = self.db.query(Employee).filter(Employee.email == email).first()
        return employee
