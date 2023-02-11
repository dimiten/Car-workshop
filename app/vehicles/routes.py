from fastapi import APIRouter
from app.vehicles.controller import VehicleController
from app.vehicles.schemas import *

vehicle_router = APIRouter(tags=["Vehicles"], prefix="/api/vehicles")


@vehicle_router.post("/add-new-vehicle", response_model=VehicleSchema)
def create_vehicle(vehicle: VehicleSchemaIn):
    return VehicleController.create_vehicle(vehicle.license_plate, vehicle.manufacturer, vehicle.model,
                                            vehicle.manufacture_year, vehicle.customer_id)


@vehicle_router.get("/id", response_model=VehicleSchema)
def get_vehicle_by_id(vehicle_id: str):
    return VehicleController.get_vehicle_by_id(vehicle_id)


@vehicle_router.get("/get-all-vehicles", response_model=list[VehicleSchema])
def get_all_vehicles():
    return VehicleController.get_all_vehicles()


@vehicle_router.put("/update", response_model=VehicleSchema)
def update_vehicle(vehicle_id: str, license_plate: str = None, manufacturer: str = None, model: str = None,
                   manufacture_year: str = None, customer_id: str = None):
    return VehicleController.update_vehicle(vehicle_id, license_plate, manufacturer, model,
                                            manufacture_year, customer_id)


@vehicle_router.delete("/")
def delete_vehicle_by_id(vehicle_id: str):
    return VehicleController.delete_vehicle_by_id(vehicle_id)
