"""Routes for Customer"""


from enum import Enum
from fastapi import APIRouter
from app.customers.controller import CustomerController
from app.customers.schemas import *
from app.vehicles.schemas import VehicleSchema


customer_router = APIRouter(tags=["Customers"], prefix="/api/customers")


class Month(str, Enum):
    """Enum for Month"""
    JANUARY = "01"
    FEBRUARY = "02"
    MARCH = "03"
    APRIL = "04"
    MAY = "05"
    JUNE = "06"
    JULY = "07"
    AUGUST = "08"
    SEPTEMBER = "09"
    OCTOBER = "10"
    NOVEMBER = "11"
    DECEMBER = "12"


@customer_router.post("/add-new-customer", response_model=CustomerSchema)
def create_customer(customer: CustomerSchemaIn):
    """Creates a customer"""
    return CustomerController.create_customer(customer.name, customer.surname, customer.email,
                                              customer.phone_number, customer.date_of_registration)


@customer_router.get("/id", response_model=CustomerSchema)
def get_customer_by_id(customer_id: str):
    """Returns customer by id"""
    return CustomerController.get_customer_by_id(customer_id)


@customer_router.get("/get-all-customers", response_model=list[CustomerSchema])
def get_all_customers():
    """Returns all customers"""
    return CustomerController.get_all_customers()


@customer_router.put("/update/is_regular", response_model=CustomerSchema)
def update_customer_is_regular(customer_id: str, customer_is_regular: bool):
    """Updates a customer attribute: is_regular"""
    return CustomerController.update_customer_is_regular(customer_id, customer_is_regular)


@customer_router.delete("/")
def delete_customer_by_id(customer_id: str):
    """Deletes a customer by id"""
    return CustomerController.delete_customer_by_id(customer_id)


@customer_router.get("get-all-vehicles-from-customer", response_model=list[VehicleSchema])
def get_all_vehicles_from_customer(customer_id: str):
    """Returns all vehicles from customer"""
    return CustomerController.get_all_vehicles_from_customer(customer_id)


@customer_router.get("get-new-customers-for-month", response_model=NumberNewCustomersSchema)
def get_new_customers_for_month(number_of_month: Month, year: str):
    """Returns customers that are registered in a specific month"""
    return CustomerController.get_new_customers_for_month(number_of_month, year)


@customer_router.get("get-new-customers-for-year", response_model=NumberNewCustomersSchema)
def get_new_customers_for_year(year: str):
    """Returns customers that are registered in a specific year"""
    return CustomerController.get_new_customers_for_year(year)


@customer_router.get("get-customers-for-years", response_model=int)
def get_customers_for_years(number_of_years: int):
    """Returns customers that are registered for at least number_of_years years"""
    return CustomerController.get_customers_for_years(number_of_years)
