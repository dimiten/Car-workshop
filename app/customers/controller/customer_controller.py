"""Customer Controller"""

from datetime import date
from fastapi import HTTPException, Response
from app.customers.services import CustomerServices
from app.customers.exceptions import *


class CustomerController:
    """CustomerController class"""

    @staticmethod
    def create_customer(name: str, surname: str, email: str, phone_number: str, date_of_registration: date):
        """Creates a customer"""
        try:
            customer = CustomerServices.create_customer(name, surname, email, phone_number, date_of_registration)
            return customer
        except CustomerEmailException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except CustomerPhoneNumberException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_customer_by_id(customer_id: str):
        """Returns customer by id"""
        customer = CustomerServices.get_customer_by_id(customer_id)
        if customer:
            return customer
        raise HTTPException(status_code=400, detail=f"Customer with provided id: {customer_id} does not exist")

    @staticmethod
    def get_all_customers():
        """Returns all customers"""
        customers = CustomerServices.get_all_customers()
        return customers

    @staticmethod
    def delete_customer_by_id(customer_id: str):
        """Deletes a customer by id"""
        customer = CustomerServices.get_customer_by_id(customer_id)
        if customer:
            CustomerServices.delete_customer_by_id(customer_id)
            return Response(content=f"Customer with id - {customer_id} is deleted")
        raise HTTPException(status_code=400, detail=f"Customer with provided id: {customer_id} does not exist")

    @staticmethod
    def update_customer_is_regular(customer_id: str, is_regular: bool):
        """Updates a customer attribute: is_regular"""
        customer = CustomerServices.get_customer_by_id(customer_id)
        if customer:
            return CustomerServices.update_customer_is_regular(customer_id, is_regular)
        raise HTTPException(status_code=400, detail=f"Customer with provided id: {customer_id} does not exist")

    @staticmethod
    def get_all_vehicles_from_customer(customer_id: str):
        """Returns all vehicles from customer"""
        customer = CustomerServices.get_customer_by_id(customer_id)
        if not customer:
            raise HTTPException(status_code=400, detail=f"Customer with provided id: {customer_id} does not exist")

        vehicles = CustomerServices.get_all_vehicles_from_customer(customer_id)
        if vehicles:
            return CustomerServices.get_all_vehicles_from_customer(customer_id)
        raise HTTPException(status_code=400,
                            detail=f"Customer with provided id: {customer_id} doesn't have any vehicles")

    @staticmethod
    def get_new_customers_for_month(number_of_month: str, year: str):
        """Returns customers that are registered in a specific month"""
        new_customers = CustomerServices.get_new_customers_for_month(number_of_month, year)
        if new_customers:
            return new_customers
        raise HTTPException(status_code=400,
                            detail=f"There are no new customers for provided number of month: {number_of_month}"
                                   f", and year: {year}")

    @staticmethod
    def get_new_customers_for_year(year: str):
        """Returns customers that are registered in a specific year"""
        new_customers = CustomerServices.get_new_customers_for_year(year)
        if new_customers:
            return new_customers
        raise HTTPException(status_code=400,
                            detail=f"There are no new customers for provided "
                                   f"year: {year}")

    @staticmethod
    def get_customers_for_years(number_of_years: int):
        """Returns customers that are registered for at least number_of_years years"""
        customers = CustomerServices.get_customers_for_years(number_of_years)
        if customers:
            return customers
        raise HTTPException(status_code=400,
                            detail=f"There are no new customers for provided number of "
                                   f"years: {number_of_years}")
