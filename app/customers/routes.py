from fastapi import APIRouter
from app.customers.controller import CustomerController
from app.customers.schemas import *
from app.vehicles.schemas import VehicleSchema
from enum import Enum

customer_router = APIRouter(tags=["Customers"], prefix="/api/customers")


class Month(str, Enum):
    January = "01"
    February = "02"
    March = "03"
    April = "04"
    May = "05"
    June = "06"
    July = "07"
    August = "08"
    September = "09"
    October = "10"
    November = "11"
    December = "12"


@customer_router.post("/add-new-customer", response_model=CustomerSchema)
def create_customer(customer: CustomerSchemaIn):
    return CustomerController.create_customer(customer.name, customer.surname, customer.email,
                                              customer.phone_number, customer.date_of_registration)


@customer_router.get("/id", response_model=CustomerSchema)
def get_customer_by_id(customer_id: str):
    return CustomerController.get_customer_by_id(customer_id)


@customer_router.get("/get-all-customers", response_model=list[CustomerSchema])
def get_all_customers():
    return CustomerController.get_all_customers()


@customer_router.put("/update/is_regular", response_model=CustomerSchema)
def update_customer_is_regular(customer_id: str, customer_is_regular: bool):
    return CustomerController.update_customer_is_regular(customer_id, customer_is_regular)


@customer_router.delete("/")
def delete_customer_by_id(customer_id: str):
    return CustomerController.delete_customer_by_id(customer_id)


@customer_router.get("get-all-vehicles-from-customer", response_model=list[VehicleSchema])
def get_all_vehicles_from_customer(customer_id: str):
    return CustomerController.get_all_vehicles_from_customer(customer_id)


@customer_router.get("get-new-customers-for-month", response_model=NumberNewCustomersSchema)
def get_new_customers_for_month(number_of_month: Month, year: str):
    return CustomerController.get_new_customers_for_month(number_of_month, year)


@customer_router.get("get-new-customers-for-year", response_model=NumberNewCustomersSchema)
def get_new_customers_for_year(year: str):
    return CustomerController.get_new_customers_for_year(year)
