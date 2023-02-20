from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.customers.models import Customer
from app.vehicles.models import Vehicle
from datetime import date


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_customer(self, name: str, surname: str, email: str, phone_number: str, date_of_registration: date):
        try:
            customer = Customer(name, surname, email, phone_number, date_of_registration)
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

    def get_all_vehicles_from_customer(self, customer_id: str):
        try:
            vehicles = self.db.query(Vehicle).filter(Vehicle.customer_id == customer_id).all()
            return vehicles
        except Exception as e:
            raise e

    def get_new_customers_for_month(self, number_of_month: str, year: str):
        try:
            new_customers_for_month = self.db.query(func.count(Customer.id).label("number_of_new_customers")).\
                filter(Customer.date_of_registration.like(f"{year}-{number_of_month}-%")).first()
            return new_customers_for_month
        except Exception as e:
            raise e

    def get_new_customers_for_year(self, year: str):
        try:
            new_customers_for_month = self.db.query(func.count(Customer.id).label("number_of_new_customers")).\
                filter(Customer.date_of_registration.like(f"{year}-%-%")).first()
            return new_customers_for_month
        except Exception as e:
            raise e

