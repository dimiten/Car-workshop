from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.customers.models import Customer


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_customer(self, name, surname, email, phone_number):
        try:
            customer = Customer(name, surname, email, phone_number)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except IntegrityError as e:
            raise e

    def get_customer_by_id(self, customer_id: str):
        try:
            customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
            return customer
        except Exception as e:
            raise e

    def get_all_customers(self):
        try:
            customers = self.db.query(Customer).all()
            return customers
        except Exception as e:
            raise e

    def delete_customer_by_id(self, customer_id: str):
        try:
            customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
            self.db.delete(customer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_customer_is_regular(self, customer_id: str, is_regular: bool):
        try:
            customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
            customer.is_regular = is_regular
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except Exception as e:
            raise e

    def get_customers_emails(self):
        try:
            customers_emails = self.db.query(Customer.email).all()
            return [item for t in customers_emails for item in t]
        except Exception as e:
            raise e

    def get_customers_phone_numbers(self):
        try:
            customers_phone_numbers = self.db.query(Customer.phone_number).all()
            return [item for t in customers_phone_numbers for item in t]
        except Exception as e:
            raise e
