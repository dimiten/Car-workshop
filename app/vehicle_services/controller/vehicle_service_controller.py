"""Vehicle service controller"""


from datetime import date

from app.vehicle_services.services import VehicleServicesServices
from fastapi import HTTPException, Response
from app.vehicle_services.exceptions import *


class VehicleServiceController:
    """VehicleServiceController class"""

    @staticmethod
    def create_vehicle_service(date_of_service: date, vehicle_id: str, employee_id: str, service_type_name: str):
        """Creates vehicle service"""
        try:
            vehicle_service = VehicleServicesServices.create_vehicle_service(date_of_service, vehicle_id, employee_id,
                                                                             service_type_name)
            return vehicle_service
        except InvalidVehicleException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except InvalidEmployeeException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except InvalidServiceTypeException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_vehicle_service_by_id(vehicle_service_id: str):
        """Get vehicle service by id"""
        vehicle_service = VehicleServicesServices.get_vehicle_service_by_id(vehicle_service_id)
        if vehicle_service:
            return vehicle_service
        raise HTTPException(status_code=400,
                            detail=f"Vehicle service with provided id: {vehicle_service_id} does not exist")

    @staticmethod
    def get_all_vehicle_services():
        """Get all vehicle services"""
        try:
            vehicle_services = VehicleServicesServices.get_all_vehicle_services()
            return vehicle_services
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_vehicle_service_by_id(vehicle_service_id: str):
        """Delete vehicle service by id"""
        vehicle_service = VehicleServicesServices.get_vehicle_service_by_id(vehicle_service_id)
        if vehicle_service:
            VehicleServicesServices.delete_vehicle_service_by_id(vehicle_service_id)
            return Response(content=f"Vehicle service with id - {vehicle_service_id} is deleted")
        raise HTTPException(status_code=400,
                            detail=f"Vehicle service with provided id: {vehicle_service_id} does not exist")

    @staticmethod
    def update_vehicle_service(vehicle_service_id: str, date_of_service: str = None, vehicle_id: str = None,
                               employee_id: str = None, service_type_name: str = None):
        """Update vehicle service"""
        vehicle_service = VehicleServicesServices.get_vehicle_service_by_id(vehicle_service_id)
        if vehicle_service:
            return VehicleServicesServices.update_vehicle_service(vehicle_service_id, date_of_service, vehicle_id,
                                                                  employee_id, service_type_name)
        raise HTTPException(status_code=400,
                            detail=f"Vehicle service with provided id: {vehicle_service_id} does not exist")

    @staticmethod
    def get_number_of_services_for_month(number_of_month: str, year: str):
        """Get number of vehicle services for specific month"""
        number_of_services = VehicleServicesServices.get_number_of_services_for_month(number_of_month, year)
        if number_of_services:
            return VehicleServicesServices.get_number_of_services_for_month(number_of_month, year)
        raise HTTPException(status_code=400,
                            detail=f"There are no services for provided number of month: {number_of_month}"
                                   f", and year: {year}")

    @staticmethod
    def get_number_of_services_for_year(year: str):
        """Get number of vehicle services for a specific year"""
        number_of_services = VehicleServicesServices.get_number_of_services_for_year(year)
        if number_of_services:
            return VehicleServicesServices.get_number_of_services_for_year(year)
        raise HTTPException(status_code=400,
                            detail=f"There are no services for provided year: {year}")

    @staticmethod
    def get_income_for_month(number_of_month: str, year: str):
        """Get income for specific month"""
        income_for_month = VehicleServicesServices.get_income_for_month(number_of_month, year)
        if income_for_month[0] is None:
            raise HTTPException(status_code=400,
                                detail=f"There is no income for provided number of month: {number_of_month}"
                                       f", and year: {year}")
        return VehicleServicesServices.get_income_for_month(number_of_month, year)

    @staticmethod
    def get_income_for_year(year: str):
        """Get income for specific year"""
        income_for_year = VehicleServicesServices.get_income_for_year(year)
        if income_for_year[0] is None:
            raise HTTPException(status_code=400,
                                detail=f"There is no income for provided year: {year}")
        return VehicleServicesServices.get_income_for_year(year)

    @staticmethod
    def get_most_popular_service_for_month(number_of_month: str, year: str):
        """Get the most popular service for a specific month"""
        most_popular_service = VehicleServicesServices.get_most_popular_service_for_month(number_of_month, year)
        if most_popular_service:
            return most_popular_service
        raise HTTPException(status_code=400,
                            detail=f"There are no services for provided number of month: {number_of_month}"
                                   f", and year: {year}")

    @staticmethod
    def get_most_popular_service_for_year(year: str):
        """Get the most popular service for a specific year"""
        most_popular_service = VehicleServicesServices.get_most_popular_service_for_year(year)
        if most_popular_service:
            return most_popular_service
        raise HTTPException(status_code=400,
                            detail=f"There are no services for provided year: {year}")
