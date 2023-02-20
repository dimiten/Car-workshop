from app.customers.repositories import CustomerRepository
from app.db.database import SessionLocal
from app.customers.exceptions import *
from datetime import date


class CustomerServices:

    @staticmethod
    def create_customer(name: str, surname: str, email: str, phone_number: str, date_of_registration: date):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                if email in customer_repository.get_customers_emails():
                    raise CustomerEmailException(status_code=400,
                                                 detail=f"Customer with provided email - {email} already exists.")
                if phone_number in customer_repository.get_customers_phone_numbers():
                    raise CustomerPhoneNumberException(status_code=400,
                                                       detail=f"Customer with provided phone number - {phone_number} "
                                                              f"already exists.")
                return customer_repository.create_customer(name, surname, email, phone_number, date_of_registration)
        except Exception as e:
            raise e

    @staticmethod
    def get_customer_by_id(customer_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_customer_by_id(customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_customers():
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_all_customers()
        except Exception as e:
            raise e

    @staticmethod
    def delete_customer_by_id(customer_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.delete_customer_by_id(customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_customer_is_regular(customer_id: str, is_regular: bool):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.update_customer_is_regular(customer_id, is_regular)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_vehicles_from_customer(customer_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_all_vehicles_from_customer(customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_new_customers_for_month(number_of_month: str, year: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_new_customers_for_month(number_of_month, year)
        except Exception as e:
            raise e

    @staticmethod
    def get_new_customers_for_year(year: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_new_customers_for_year(year)
        except Exception as e:
            raise e

    @staticmethod
    def get_customers_for_years(number_of_years: int):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.get_customers_for_years(number_of_years)
        except Exception as e:
            raise e
