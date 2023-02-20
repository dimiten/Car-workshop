from datetime import date

from app.vehicle_services.repositories import VehicleServiceRepository
from app.db.database import SessionLocal
from app.vehicles.repositories import VehicleRepository
from app.employees.repositories import EmployeeRepository
from app.service_types.repositories import ServiceTypeRepository
from app.vehicle_services.exceptions import *


class VehicleServicesServices:

    @staticmethod
    def create_vehicle_service(date_of_service: date, vehicle_id: str, employee_id: str, service_type_name: str):
        try:
            # datetime.datetime.strptime(str(date_of_service), r"%Y-%m-%d")
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                vehicle_repository = VehicleRepository(db)
                if not vehicle_repository.get_vehicle_by_id(vehicle_id):
                    raise InvalidVehicleException(status_code=400,
                                                  detail=f"Vehicle with provided id: {vehicle_id} does not exist")
                employee_repository = EmployeeRepository(db)
                if not employee_repository.get_employee_by_id(employee_id):
                    raise InvalidEmployeeException(status_code=400,
                                                   detail=f"Employee with provided id: {employee_id} does not exist")
                service_type_repository = ServiceTypeRepository(db)
                if not service_type_repository.get_service_type_by_name(service_type_name):
                    raise InvalidServiceTypeException(status_code=400,
                                                      detail=f"Service type with provided name: {service_type_name}"
                                                             f" does not exist")
                return vehicle_service_repository.create_vehicle_service(date_of_service, vehicle_id, employee_id,
                                                                         service_type_name)
        except Exception as e:
            raise e

    @staticmethod
    def get_vehicle_service_by_id(vehicle_service_id: str):
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.get_vehicle_service_by_id(vehicle_service_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_vehicle_services():
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.get_all_vehicle_services()
        except Exception as e:
            raise e

    @staticmethod
    def delete_vehicle_service_by_id(vehicle_service_id: str):
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.delete_vehicle_service_by_id(vehicle_service_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_vehicle_service(vehicle_service_id: str, date_of_service: str = None, vehicle_id: str = None,
                               employee_id: str = None, service_type_name: str = None):
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.update_vehicle_service(vehicle_service_id, date_of_service,
                                                                         vehicle_id, employee_id, service_type_name)
        except Exception as e:
            raise e

    @staticmethod
    def get_number_of_services_for_month(number_of_month: str, year: str):
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.get_number_of_services_for_month(number_of_month, year)
        except Exception as e:
            raise e

    @staticmethod
    def get_number_of_services_for_year(year: str):
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.get_number_of_services_for_year(year)
        except Exception as e:
            raise e

    @staticmethod
    def get_income_for_month(number_of_month: str, year: str):
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.get_income_for_month(number_of_month, year)
        except Exception as e:
            raise e

    @staticmethod
    def get_income_for_year(year: str):
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.get_income_for_year(year)
        except Exception as e:
            raise e

    @staticmethod
    def get_most_popular_service_for_month(number_of_month: str, year: str):
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.get_most_popular_service_for_month(number_of_month, year)
        except Exception as e:
            raise e

    @staticmethod
    def get_most_popular_service_for_year(year: str):
        try:
            with SessionLocal() as db:
                vehicle_service_repository = VehicleServiceRepository(db)
                return vehicle_service_repository.get_most_popular_service_for_year(year)
        except Exception as e:
            raise e
