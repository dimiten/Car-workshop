"""Vehicle controller"""


from app.vehicles.services import VehicleServices
from fastapi import HTTPException, Response
from app.vehicles.exceptions import *


class VehicleController:
    """VehicleController class"""

    @staticmethod
    def create_vehicle(license_plate: str, manufacturer: str, model: str, manufacture_year: str, customer_id: str):
        """Create a vehicle"""
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
        """Get a vehicle by id"""
        vehicle = VehicleServices.get_vehicle_by_id(vehicle_id)
        if vehicle:
            return vehicle
        raise HTTPException(status_code=400, detail=f"Vehicle with provided id: {vehicle_id} does not exist")

    @staticmethod
    def get_all_vehicles():
        """Get all vehicles"""
        vehicles = VehicleServices.get_all_vehicles()
        return vehicles

    @staticmethod
    def delete_vehicle_by_id(vehicle_id: str):
        """Delete a vehicle by id"""
        vehicle = VehicleServices.get_vehicle_by_id(vehicle_id)
        if vehicle:
            VehicleServices.delete_vehicle_by_id(vehicle_id)
            return Response(content=f"Vehicle with id - {vehicle_id} is deleted")
        raise HTTPException(status_code=400, detail=f"Vehicle with provided id: {vehicle_id} does not exist")

    @staticmethod
    def update_vehicle(vehicle_id: str, license_plate: str = None, manufacturer: str = None, model: str = None,
                       manufacture_year: str = None, customer_id: str = None):
        """Update a vehicle"""
        vehicle = VehicleServices.get_vehicle_by_id(vehicle_id)
        if vehicle:
            return VehicleServices.update_vehicle(vehicle_id, license_plate, manufacturer, model,
                                                  manufacture_year, customer_id)
        raise HTTPException(status_code=400, detail=f"Vehicle with provided id: {vehicle_id} does not exist")

    @staticmethod
    def get_vehicles_by_manufacture_year(manufacture_year: str):
        """Get vehicles by year of manufacture"""
        vehicles = VehicleServices.get_all_vehicles_by_manufacture_year(manufacture_year)
        if vehicles:
            return vehicles
        raise HTTPException(status_code=400, detail=f"There are no vehicles with provided year: {manufacture_year}")

    @staticmethod
    def get_vehicles_by_manufacturer(manufacturer: str):
        """Get vehicles by manufacturer"""
        vehicles = VehicleServices.get_all_vehicles_by_manufacturer(manufacturer)
        if vehicles:
            return vehicles
        raise HTTPException(status_code=400,
                            detail=f"There are no vehicles with provided manufacturer: {manufacturer}")

    @staticmethod
    def get_vehicles_by_model(manufacturer: str, model: str):
        """Get vehicles by model"""
        vehicles = VehicleServices.get_all_vehicles_by_model(manufacturer, model)
        if vehicles:
            return vehicles
        raise HTTPException(status_code=400,
                            detail=f"There are no vehicles with provided manufacturer: {manufacturer}"
                                   f" and model: {model}")
