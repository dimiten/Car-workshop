from fastapi import APIRouter
from app.vehicle_services.controller import VehicleServiceController
from app.vehicle_services.schemas import *

vehicle_service_router = APIRouter(tags=["Vehicle services"], prefix="/api/vehicle-services")


@vehicle_service_router.post("/add-new-vehicle-service", response_model=VehicleServiceSchema)
def create_vehicle_service(vehicle_service: VehicleServiceSchemaIn):
    return VehicleServiceController.create_vehicle_service(vehicle_service.date_of_service, vehicle_service.vehicle_id,
                                                           vehicle_service.employee_id,
                                                           vehicle_service.service_type_name)


@vehicle_service_router.get("/id", response_model=VehicleServiceSchema)
def get_vehicle_service_by_id(vehicle_service_id: str):
    return VehicleServiceController.get_vehicle_service_by_id(vehicle_service_id)


@vehicle_service_router.get("/get-all-vehicle-services", response_model=list[VehicleServiceSchema])
def get_all_vehicle_services():
    return VehicleServiceController.get_all_vehicle_services()


@vehicle_service_router.put("/update", response_model=VehicleServiceSchema)
def update_vehicle_service(vehicle_service_id: str, date_of_service: str = None, vehicle_id: str = None,
                           employee_id: str = None, service_type_name: str = None):
    return VehicleServiceController.update_vehicle_service(vehicle_service_id, date_of_service, vehicle_id, employee_id,
                                                           service_type_name)


@vehicle_service_router.delete("/")
def delete_vehicle_service_by_id(vehicle_service_id: str):
    return VehicleServiceController.delete_vehicle_service_by_id(vehicle_service_id)


@vehicle_service_router.get("/get-number-of-services-for-month", response_model=int)
def get_number_of_services_for_month(number_of_month: str):
    return VehicleServiceController.get_number_of_services_for_month(number_of_month)
