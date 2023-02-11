from app.customers.services import CustomerServices
from fastapi import HTTPException, Response
from app.customers.exceptions import *


class CustomerController:

    @staticmethod
    def create_customer(name: str, surname: str, email: str, phone_number: str):
        try:
            customer = CustomerServices.create_customer(name, surname, email, phone_number)
            return customer
        except CustomerEmailException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except CustomerPhoneNumberException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_customer_by_id(customer_id: str):
        customer = CustomerServices.get_customer_by_id(customer_id)
        if customer:
            return customer
        else:
            raise HTTPException(status_code=400, detail=f"Customer with provided id: {customer_id} does not exist")

    @staticmethod
    def get_all_customers():
        customers = CustomerServices.get_all_customers()
        return customers

    @staticmethod
    def delete_customer_by_id(customer_id: str):
        customer = CustomerServices.get_customer_by_id(customer_id)
        if customer:
            CustomerServices.delete_customer_by_id(customer_id)
            return Response(content=f"Customer with id - {customer_id} is deleted")
        else:
            raise HTTPException(status_code=400, detail=f"Customer with provided id: {customer_id} does not exist")

    @staticmethod
    def update_customer_is_regular(customer_id: str, is_regular: bool):
        customer = CustomerServices.get_customer_by_id(customer_id)
        if customer:
            return CustomerServices.update_customer_is_regular(customer_id, is_regular)
        else:
            raise HTTPException(status_code=400, detail=f"Customer with provided id: {customer_id} does not exist")
