import pytest
from sqlalchemy.exc import IntegrityError
import datetime

from app.tests import TestClass, TestingSessionLocal
from app.customers.repositories import CustomerRepository
from app.vehicles.repositories import VehicleRepository


class TestCustomerRepo(TestClass):

    def create_customers_for_methods(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            date = datetime.datetime(2023, 2, 20)
            customer_repository.create_customer("Ime1", "Prezime1", "email1@gmail.com", "+3813891383", date)
            customer_repository.create_customer("Ime2", "Prezime2", "email2@gmail.com", "+3813459183", date)
            customer_repository.create_customer("Ime3", "Prezime3", "email3@gmail.com", "+3813131321", date)
            customer_repository.create_customer("Ime4", "Prezime4", "email4@gmail.com", "+3813989868", date)

    def test_create_customer(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            date = datetime.date(2023, 2, 20)
            customer = customer_repository.create_customer("Marko", "Savic", "markosavic@gmail.com",
                                                           "+38193193193", date)
            assert customer.name == "Marko"
            assert customer.surname == "Savic"
            assert customer.email == "markosavic@gmail.com"
            assert customer.phone_number == "+38193193193"
            assert customer.date_of_registration == date
            assert customer.is_regular is False

    def test_create_customer_fail(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            date = datetime.date(2023, 2, 20)
            customer = customer_repository.create_customer("Marko", "Savic",
                                                           "markosavic@gmail.com", "+38193193193", date)
            assert not customer.name != "Marko"
            assert not customer.surname != "Savic"
            assert not customer.email != "markosavic@gmail.com"
            assert not customer.phone_number != "+38193193193"
            assert not customer.date_of_registration != date
            assert customer.is_regular is not True
            with pytest.raises(IntegrityError) as e:
                customer = customer_repository.create_customer("Marko", "Savic",
                                                               "markosavic@gmail.com", "+38193193193", date)

    def test_get_customer_by_id(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            date = datetime.datetime(2023, 2, 20)
            customer = customer_repository.create_customer("Marko", "Savic",
                                                           "markosavic@gmail.com", "+38193193193", date)
            customer2 = customer_repository.get_customer_by_id(customer.id)
            assert customer == customer2

    def test_get_customer_by_id_fail(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            date = datetime.datetime(2023, 2, 20)
            customer = customer_repository.create_customer("Marko", "Savic",
                                                           "markosavic@gmail.com", "+38193193193", date)
            customer2 = customer_repository.get_customer_by_id(customer.id)
            assert not customer != customer2

    def test_get_all_customers(self):
        self.create_customers_for_methods()
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            customers = customer_repository.get_all_customers()
            assert len(customers) == 4

    def test_get_all_customers_fail(self):
        self.create_customers_for_methods()
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            customers = customer_repository.get_all_customers()
            assert not len(customers) != 4

    def test_delete_customer_by_id(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            date = datetime.datetime(2023, 2, 20)
            customer = customer_repository.create_customer("Marko", "Savic",
                                                           "markosavic@gmail.com", "+38193193193", date)
            assert customer_repository.delete_customer_by_id(customer.id) is True

    def test_delete_customer_by_id_fail(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            date = datetime.datetime(2023, 2, 20)
            customer = customer_repository.create_customer("Marko", "Savic",
                                                           "markosavic@gmail.com", "+38193193193", date)
            assert customer_repository.delete_customer_by_id(customer.id) is not False

    def test_update_customer_is_regular(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            date = datetime.datetime(2023, 2, 20)
            customer = customer_repository.create_customer("Marko", "Savic",
                                                           "markosavic@gmail.com", "+38193193193", date)
            customer_repository.update_customer_is_regular(customer.id, True)
            assert customer.is_regular is True

    def test_update_customer_is_regular_fail(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            date = datetime.datetime(2023, 2, 20)
            customer = customer_repository.create_customer("Marko", "Savic",
                                                           "markosavic@gmail.com", "+38193193193", date)
            customer_repository.update_customer_is_regular(customer.id, True)
            assert customer.is_regular is not False

    def test_get_customers_emails(self):
        self.create_customers_for_methods()
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            customers_emails = customer_repository.get_customers_emails()
            assert {"email1@gmail.com", "email2@gmail.com", "email3@gmail.com", "email4@gmail.com"} == \
                   set(customers_emails)

    def test_get_customers_emails_fail(self):
        self.create_customers_for_methods()
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            customers_emails = customer_repository.get_customers_emails()
            assert not {"email1@gmail.com", "email2@gmail.com", "email3@gmail.com", "email4@gmail.com"} != \
                   set(customers_emails)

    def test_get_customers_phone_numbers(self):
        self.create_customers_for_methods()
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            customers_phone_numbers = customer_repository.get_customers_phone_numbers()
            assert {"+3813891383", "+3813459183", "+3813131321", "+3813989868"} == set(customers_phone_numbers)

    def test_get_customers_phone_numbers_fail(self):
        self.create_customers_for_methods()
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            customers_phone_numbers = customer_repository.get_customers_phone_numbers()
            assert not {"+3813891383", "+3813459183", "+3813131321", "+3813989868"} != set(customers_phone_numbers)

    def test_get_all_vehicles_from_customer(self):
        with TestingSessionLocal() as db:
            date = datetime.datetime(2023, 2, 20)
            customer_repository = CustomerRepository(db)
            vehicle_repository = VehicleRepository(db)
            customer = customer_repository.create_customer("Marko", "Savic",
                                                           "markosavic@gmail.com", "+38193193193", date)
            vehicle_repository.create_vehicle("hgh0313", "BMW", "M5", "2017", customer.id)
            vehicle_repository.create_vehicle("mnb0313", "BMW", "M7", "2010", customer.id)
            vehicle_repository.create_vehicle("zxc0313", "BMW", "M3", "2019", customer.id)

            customers_vehicles = customer_repository.get_all_vehicles_from_customer(customer.id)

            assert len(customers_vehicles) == 3

    def test_get_all_vehicles_from_customer_fail(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            vehicle_repository = VehicleRepository(db)
            date = datetime.datetime(2023, 2, 20)
            customer = customer_repository.create_customer("Marko", "Savic",
                                                           "markosavic@gmail.com", "+38193193193", date)
            vehicle_repository.create_vehicle("hgh0313", "BMW", "M5", "2017", customer.id)
            vehicle_repository.create_vehicle("mnb0313", "BMW", "M7", "2010", customer.id)
            vehicle_repository.create_vehicle("zxc0313", "BMW", "M3", "2019", customer.id)

            customers_vehicles = customer_repository.get_all_vehicles_from_customer(customer.id)

            assert not len(customers_vehicles) != 3
