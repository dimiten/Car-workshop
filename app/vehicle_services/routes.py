from fastapi import APIRouter
from app.vehicle_services.controller import VehicleServiceController
from app.vehicle_services.schemas import *
from enum import Enum
from datetime import date

vehicle_service_router = APIRouter(tags=["Vehicle services"], prefix="/api/vehicle-services")


class Month(str, Enum):
    January = "01"
    February = "02"
    March = "03"
    April = "04"
    May = "05"
    June = "06"
    July = "07"
    August = "08"
    September = "09"
    October = "10"
    November = "11"
    December = "12"


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


@vehicle_service_router.get("/get-number-of-services-for-month", response_model=list[VehicleServiceCountSchema])
def get_number_of_services_for_month(number_of_month: Month, year: str):
    return VehicleServiceController.get_number_of_services_for_month(number_of_month, year)


@vehicle_service_router.get("/get-number-of-services-for-year", response_model=list[VehicleServiceCountSchema])
def get_number_of_services_for_year(year: str):
    return VehicleServiceController.get_number_of_services_for_year(year)


@vehicle_service_router.get("/get-income-for-month", response_model=VehicleServiceMonthIncomeSchema)
def get_income_for_month(number_of_month: Month, year: str):
    return VehicleServiceController.get_income_for_month(number_of_month, year)


@vehicle_service_router.get("/get-income-for-year", response_model=VehicleServiceYearIncomeSchema)
def get_income_for_year(year: str):
    return VehicleServiceController.get_income_for_year(year)
