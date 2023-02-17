from app.vehicles.repositories import VehicleRepository
from app.db.database import SessionLocal
from app.vehicles.exceptions import *
from app.customers.repositories import CustomerRepository


class VehicleServices:

    @staticmethod
    def create_vehicle(license_plate, manufacturer, model, manufacture_year, customer_id):
        try:
            with SessionLocal() as db:
                vehicle_repository = VehicleRepository(db)
                if license_plate in vehicle_repository.get_vehicles_license_plates():
                    raise VehicleLicensePlateException(status_code=400,
                                                       detail=f"Vehicle with license plate: {license_plate} "
                                                              f"already exists")
                customer_repository = CustomerRepository(db)
                if customer_repository.get_customer_by_id(customer_id):
                    return vehicle_repository.create_vehicle(license_plate, manufacturer, model, manufacture_year,
                                                             customer_id)
                raise InvalidCustomerIdException(status_code=400,
                                                 detail=f"Customer with provided id: {customer_id} does not exist")
        except Exception as e:
            raise e

    @staticmethod
    def get_vehicle_by_id(vehicle_id: str):
        try:
            with SessionLocal() as db:
                vehicle_repository = VehicleRepository(db)
                return vehicle_repository.get_vehicle_by_id(vehicle_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_vehicles():
        try:
            with SessionLocal() as db:
                vehicle_repository = VehicleRepository(db)
                return vehicle_repository.get_all_vehicles()
        except Exception as e:
            raise e

    @staticmethod
    def delete_vehicle_by_id(vehicle_id: str):
        try:
            with SessionLocal() as db:
                vehicle_repository = VehicleRepository(db)
                return vehicle_repository.delete_vehicle_by_id(vehicle_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_vehicle(vehicle_id: str, license_plate: str = None, manufacturer: str = None, model: str = None,
                       manufacture_year: str = None, customer_id: str = None):
        try:
            with SessionLocal() as db:
                vehicle_repository = VehicleRepository(db)
                return vehicle_repository.update_vehicle(vehicle_id, license_plate, manufacturer, model,
                                                         manufacture_year, customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_vehicles_by_manufacture_year(manufacture_year: str):
        try:
            with SessionLocal() as db:
                vehicle_repository = VehicleRepository(db)
                return vehicle_repository.get_all_vehicles_by_manufacture_year(manufacture_year)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_vehicles_by_manufacturer(manufacturer: str):
        try:
            with SessionLocal() as db:
                vehicle_repository = VehicleRepository(db)
                return vehicle_repository.get_all_vehicles_by_manufacturer(manufacturer)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_vehicles_by_model(manufacturer: str, model: str):
        try:
            with SessionLocal() as db:
                vehicle_repository = VehicleRepository(db)
                return vehicle_repository.get_all_vehicles_by_model(manufacturer, model)
        except Exception as e:
            raise e
