from app.customers.repositories import CustomerRepository
from app.db.database import SessionLocal


class CustomerServices:

    @staticmethod
    def create_customer(name, surname, email, phone_number):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.create_customer(name, surname, email, phone_number)
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
