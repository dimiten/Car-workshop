import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.employees.repositories import EmployeeRepository


class TestEmployeeRepo(TestClass):

    def create_employees_for_methods(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_repository.create_employee("Ime1", "Prezime1", "mejl1@gmail.com",
                                                "+3816426422", "mechanic")
            employee_repository.create_employee("Ime2", "Prezime2", "mejl2@gmail.com",
                                                "+3816495432", "mechanic")
            employee_repository.create_employee("Ime3", "Prezime3", "mejl3@gmail.com",
                                                "+3811341432", "mechanic")
            employee_repository.create_employee("Ime4", "Prezime4", "mejl4@gmail.com",
                                                "+3816431444", "mechanic")

    def test_create_employee(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee = employee_repository.create_employee("Ivan", "Petrovic", "ivanpetrovic@gmail.com",
                                                           "+3816583812", "mechanic")
            assert employee.name == "Ivan"
            assert employee.surname == "Petrovic"
            assert employee.email == "ivanpetrovic@gmail.com"
            assert employee.phone_number == "+3816583812"
            assert employee.position == "mechanic"
            assert employee.is_admin is False

    def test_create_employee_fail(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee = employee_repository.create_employee("Ivan", "Petrovic", "ivanpetrovic@gmail.com",
                                                           "+3816583812", "mechanic")
            assert not employee.name != "Ivan"
            assert not employee.surname != "Petrovic"
            assert not employee.email != "ivanpetrovic@gmail.com"
            assert not employee.phone_number != "+3816583812"
            assert not employee.position != "mechanic"
            assert employee.is_admin is not True
            with pytest.raises(IntegrityError) as e:
                employee1 = employee_repository.create_employee("Ivan", "Petrovic", "ivanpetrovic@gmail.com",
                                                                "+3816583812", "mechanic")

    def test_get_employee_by_id(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee1 = employee_repository.create_employee("Ivan", "Petrovic", "ivanpetrovic@gmail.com",
                                                            "+3816583812", "mechanic")
            employee2 = employee_repository.get_employee_by_id(employee1.id)
            assert employee1 == employee2

    def test_get_employee_by_id_fail(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee1 = employee_repository.create_employee("Ivan", "Petrovic", "ivanpetrovic@gmail.com",
                                                            "+3816583812", "mechanic")
            employee2 = employee_repository.get_employee_by_id(employee1.id)
            assert not employee1 != employee2

    def test_get_all_employees(self):
        self.create_employees_for_methods()
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employees = employee_repository.get_all_employees()
            assert len(employees) == 4

    def test_get_all_employees_fail(self):
        self.create_employees_for_methods()
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employees = employee_repository.get_all_employees()
            assert not len(employees) != 4

    def test_delete_employee_by_id(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee = employee_repository.create_employee("Ivan", "Petrovic", "ivanpetrovic@gmail.com",
                                                           "+3816583812", "mechanic")
            assert employee_repository.delete_employee_by_id(employee.id) is True

    def test_delete_employee_by_id_fail(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee = employee_repository.create_employee("Ivan", "Petrovic", "ivanpetrovic@gmail.com",
                                                           "+3816583812", "mechanic")
            assert employee_repository.delete_employee_by_id(employee.id) is not False

    def test_update_employee_is_admin(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee = employee_repository.create_employee("Ivan", "Petrovic", "ivanpetrovic@gmail.com",
                                                           "+3816583812", "mechanic")
            employee_repository.update_employee_is_admin(employee.id, True)
            assert employee.is_admin is True

    def test_update_employee_is_admin_fail(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee = employee_repository.create_employee("Ivan", "Petrovic", "ivanpetrovic@gmail.com",
                                                           "+3816583812", "mechanic")
            employee_repository.update_employee_is_admin(employee.id, True)
            assert employee.is_admin is not False

    def test_get_employees_emails(self):
        self.create_employees_for_methods()
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employees_emails = employee_repository.get_employees_emails()
            assert {"mejl1@gmail.com", "mejl2@gmail.com", "mejl3@gmail.com", "mejl4@gmail.com"} == set(
                employees_emails)

    def test_get_employees_emails_fail(self):
        self.create_employees_for_methods()
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employees_emails = employee_repository.get_employees_emails()
            assert not {"mejl1@gmail.com", "mejl2@gmail.com", "mejl3@gmail.com", "mejl4@gmail.com"} != set(
                employees_emails)

    def test_get_employees_phone_numbers(self):
        self.create_employees_for_methods()
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employees_phone_numbers = employee_repository.get_employees_phone_numbers()
            assert {"+3816426422", "+3816495432", "+3811341432", "+3816431444"} == set(employees_phone_numbers)

    def test_get_employees_phone_numbers_fail(self):
        self.create_employees_for_methods()
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employees_phone_numbers = employee_repository.get_employees_phone_numbers()
            assert not {"+3816426422", "+3816495432", "+3811341432", "+3816431444"} != set(employees_phone_numbers)
