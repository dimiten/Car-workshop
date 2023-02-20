from datetime import date

from app.vehicle_services.services import VehicleServicesServices
from fastapi import HTTPException, Response
from app.vehicle_services.exceptions import *


class VehicleServiceController:

    @staticmethod
    def create_vehicle_service(date_of_service: date, vehicle_id: str, employee_id: str, service_type_name: str):
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
        vehicle_service = VehicleServicesServices.get_vehicle_service_by_id(vehicle_service_id)
        if vehicle_service:
            return vehicle_service
        else:
            raise HTTPException(status_code=400,
                                detail=f"Vehicle service with provided id: {vehicle_service_id} does not exist")

    @staticmethod
    def get_all_vehicle_services():
        try:
            vehicle_services = VehicleServicesServices.get_all_vehicle_services()
            return vehicle_services
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_vehicle_service_by_id(vehicle_service_id: str):
        vehicle_service = VehicleServicesServices.get_vehicle_service_by_id(vehicle_service_id)
        if vehicle_service:
            VehicleServicesServices.delete_vehicle_service_by_id(vehicle_service_id)
            return Response(content=f"Vehicle service with id - {vehicle_service_id} is deleted")
        else:
            raise HTTPException(status_code=400,
                                detail=f"Vehicle service with provided id: {vehicle_service_id} does not exist")

    @staticmethod
    def update_vehicle_service(vehicle_service_id: str, date_of_service: str = None, vehicle_id: str = None,
                               employee_id: str = None, service_type_name: str = None):
        vehicle_service = VehicleServicesServices.get_vehicle_service_by_id(vehicle_service_id)
        if vehicle_service:
            return VehicleServicesServices.update_vehicle_service(vehicle_service_id, date_of_service, vehicle_id,
                                                                  employee_id, service_type_name)
        else:
            raise HTTPException(status_code=400,
                                detail=f"Vehicle service with provided id: {vehicle_service_id} does not exist")

    @staticmethod
    def get_number_of_services_for_month(number_of_month: str, year: str):
        number_of_services = VehicleServicesServices.get_number_of_services_for_month(number_of_month, year)
        if number_of_services:
            return VehicleServicesServices.get_number_of_services_for_month(number_of_month, year)
        else:
            raise HTTPException(status_code=400,
                                detail=f"There are no services for provided number of month: {number_of_month}"
                                       f", and year: {year}")

    @staticmethod
    def get_number_of_services_for_year(year: str):
        number_of_services = VehicleServicesServices.get_number_of_services_for_year(year)
        if number_of_services:
            return VehicleServicesServices.get_number_of_services_for_year(year)
        else:
            raise HTTPException(status_code=400,
                                detail=f"There are no services for provided year: {year}")

    @staticmethod
    def get_income_for_month(number_of_month: str, year: str):
        income_for_month = VehicleServicesServices.get_income_for_month(number_of_month, year)
        if income_for_month[0] is None:
            raise HTTPException(status_code=400,
                                detail=f"There is no income for provided number of month: {number_of_month}"
                                       f", and year: {year}")
        else:
            return VehicleServicesServices.get_income_for_month(number_of_month, year)

    @staticmethod
    def get_income_for_year(year: str):
        income_for_year = VehicleServicesServices.get_income_for_year(year)
        if income_for_year[0] is None:
            raise HTTPException(status_code=400,
                                detail=f"There is no income for provided year: {year}")
        else:
            return VehicleServicesServices.get_income_for_year(year)

    @staticmethod
    def get_most_popular_service_for_month(number_of_month: str, year: str):
        most_popular_service = VehicleServicesServices.get_most_popular_service_for_month(number_of_month, year)
        if most_popular_service:
            return most_popular_service
        else:
            raise HTTPException(status_code=400,
                                detail=f"There are no services for provided number of month: {number_of_month}"
                                       f", and year: {year}")

    @staticmethod
    def get_most_popular_service_for_year(year: str):
        most_popular_service = VehicleServicesServices.get_most_popular_service_for_year(year)
        if most_popular_service:
            return most_popular_service
        else:
            raise HTTPException(status_code=400,
                                detail=f"There are no services for provided year: {year}")
