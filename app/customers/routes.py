from fastapi import APIRouter
from app.customers.controller import CustomerController
from app.customers.schemas import *


customer_router = APIRouter(tags=["Customers"], prefix="/api/customers")


@customer_router.post("/add-new-customer", response_model=CustomerSchema)
def create_customer(customer: CustomerSchemaIn):
    return CustomerController.create_customer(customer.name, customer.surname, customer.email, customer.phone_number)


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
