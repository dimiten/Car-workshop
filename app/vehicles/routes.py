"""Vehicle routes"""


from fastapi import APIRouter, Depends
from app.vehicles.controller import VehicleController
from app.vehicles.schemas import *
from app.employees.controller import JWTBearer

vehicle_router = APIRouter(tags=["Vehicles"], prefix="/api/vehicles")


@vehicle_router.post("/add-new-vehicle", response_model=VehicleSchema)
def create_vehicle(vehicle: VehicleSchemaIn):
    """Create a vehicle"""
    return VehicleController.create_vehicle(vehicle.license_plate, vehicle.manufacturer, vehicle.model,
                                            vehicle.manufacture_year, vehicle.customer_id)


@vehicle_router.get("/id", response_model=VehicleSchema)
def get_vehicle_by_id(vehicle_id: str):
    """Get a vehicle by id"""
    return VehicleController.get_vehicle_by_id(vehicle_id)


@vehicle_router.get("/get-all-vehicles", response_model=list[VehicleSchema])
def get_all_vehicles():
    """Get all vehicles"""
    return VehicleController.get_all_vehicles()


@vehicle_router.put("/update", response_model=VehicleSchema)
def update_vehicle(vehicle_id: str, license_plate: str = None, manufacturer: str = None, model: str = None,
                   manufacture_year: str = None, customer_id: str = None):
    """Update a vehicle"""
    return VehicleController.update_vehicle(vehicle_id, license_plate, manufacturer, model,
                                            manufacture_year, customer_id)


@vehicle_router.delete("/", dependencies=[Depends(JWTBearer("admin"))])
def delete_vehicle_by_id(vehicle_id: str):
    """Delete a vehicle by id"""
    return VehicleController.delete_vehicle_by_id(vehicle_id)


@vehicle_router.get("/get-vehicles-by-manufacture-year", response_model=list[VehicleSchema])
def get_all_vehicles_by_manufacture_year(manufacture_year: str):
    """Get all vehicles by year of manufacturing"""
    return VehicleController.get_vehicles_by_manufacture_year(manufacture_year)


@vehicle_router.get("/get-vehicles-by-manufacturer", response_model=list[VehicleSchema])
def get_all_vehicles_by_manufacturer(manufacturer: str):
    """Get all vehicles by manufacturer"""
    return VehicleController.get_vehicles_by_manufacturer(manufacturer)


@vehicle_router.get("/get-vehicles-by-model", response_model=list[VehicleSchema])
def get_all_vehicles_by_model(manufacturer: str, model: str):
    """Get all vehicles by model"""
    return VehicleController.get_vehicles_by_model(manufacturer, model)
