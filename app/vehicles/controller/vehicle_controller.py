from app.vehicles.services import VehicleServices
from fastapi import HTTPException, Response
from app.vehicles.exceptions import *


class VehicleController:

    @staticmethod
    def create_vehicle(license_plate: str, manufacturer: str, model: str, manufacture_year: str, customer_id: str):
        try:
            vehicle = VehicleServices.create_vehicle(license_plate, manufacturer, model, manufacture_year, customer_id)
            return vehicle
        except VehicleLicensePlateException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except InvalidCustomerIdException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_vehicle_by_id(vehicle_id: str):
        vehicle = VehicleServices.get_vehicle_by_id(vehicle_id)
        if vehicle:
            return vehicle
        else:
            raise HTTPException(status_code=400, detail=f"Vehicle with provided id: {vehicle_id} does not exist")

    @staticmethod
    def get_all_vehicles():
        vehicles = VehicleServices.get_all_vehicles()
        return vehicles

    @staticmethod
    def delete_vehicle_by_id(vehicle_id: str):
        vehicle = VehicleServices.get_vehicle_by_id(vehicle_id)
        if vehicle:
            VehicleServices.delete_vehicle_by_id(vehicle_id)
            return Response(content=f"Vehicle with id - {vehicle_id} is deleted")
        else:
            raise HTTPException(status_code=400, detail=f"Vehicle with provided id: {vehicle_id} does not exist")

    @staticmethod
    def update_vehicle(vehicle_id: str, license_plate: str = None, manufacturer: str = None, model: str = None,
                       manufacture_year: str = None, customer_id: str = None):
        vehicle = VehicleServices.get_vehicle_by_id(vehicle_id)
        if vehicle:
            return VehicleServices.update_vehicle(vehicle_id, license_plate, manufacturer, model,
                                                  manufacture_year, customer_id)
        else:
            raise HTTPException(status_code=400, detail=f"Vehicle with provided id: {vehicle_id} does not exist")
