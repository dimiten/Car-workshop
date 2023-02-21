"""Vehicle services routes"""


from enum import Enum
from fastapi import APIRouter
from app.vehicle_services.controller import VehicleServiceController
from app.vehicle_services.schemas import *


vehicle_service_router = APIRouter(tags=["Vehicle services"], prefix="/api/vehicle-services")


class Month(str, Enum):
    """Month enum class"""
    JANUARY = "01"
    FEBRUARY = "02"
    MARCH = "03"
    APRIL = "04"
    MAY = "05"
    JUNE = "06"
    JULY = "07"
    AUGUST = "08"
    SEPTEMBER = "09"
    OCTOBER = "10"
    NOVEMBER = "11"
    DECEMBER = "12"


@vehicle_service_router.post("/add-new-vehicle-service", response_model=VehicleServiceSchema)
def create_vehicle_service(vehicle_service: VehicleServiceSchemaIn):
    """Create a vehicle service"""
    return VehicleServiceController.create_vehicle_service(vehicle_service.date_of_service, vehicle_service.vehicle_id,
                                                           vehicle_service.employee_id,
                                                           vehicle_service.service_type_name)


@vehicle_service_router.get("/id", response_model=VehicleServiceSchema)
def get_vehicle_service_by_id(vehicle_service_id: str):
    """Get vehicle service by id"""
    return VehicleServiceController.get_vehicle_service_by_id(vehicle_service_id)


@vehicle_service_router.get("/get-all-vehicle-services", response_model=list[VehicleServiceSchema])
def get_all_vehicle_services():
    """Get all vehicle services"""
    return VehicleServiceController.get_all_vehicle_services()


@vehicle_service_router.put("/update", response_model=VehicleServiceSchema)
def update_vehicle_service(vehicle_service_id: str, date_of_service: str = None, vehicle_id: str = None,
                           employee_id: str = None, service_type_name: str = None):
    """Update vehicle service"""
    return VehicleServiceController.update_vehicle_service(vehicle_service_id, date_of_service, vehicle_id, employee_id,
                                                           service_type_name)


@vehicle_service_router.delete("/")
def delete_vehicle_service_by_id(vehicle_service_id: str):
    """Delete vehicle service by id"""
    return VehicleServiceController.delete_vehicle_service_by_id(vehicle_service_id)


@vehicle_service_router.get("/get-number-of-services-for-month", response_model=list[VehicleServiceCountSchema])
def get_number_of_services_for_month(number_of_month: Month, year: str):
    """Get the number of services for a specific month"""
    return VehicleServiceController.get_number_of_services_for_month(number_of_month, year)


@vehicle_service_router.get("/get-number-of-services-for-year", response_model=list[VehicleServiceCountSchema])
def get_number_of_services_for_year(year: str):
    """Get the number of services for a specific year"""
    return VehicleServiceController.get_number_of_services_for_year(year)


@vehicle_service_router.get("/get-income-for-month", response_model=VehicleServiceMonthIncomeSchema)
def get_income_for_month(number_of_month: Month, year: str):
    """Get the income for a specific month"""
    return VehicleServiceController.get_income_for_month(number_of_month, year)


@vehicle_service_router.get("/get-income-for-year", response_model=VehicleServiceYearIncomeSchema)
def get_income_for_year(year: str):
    """Get the income for a specific year"""
    return VehicleServiceController.get_income_for_year(year)


@vehicle_service_router.get("/get-most-popular-service-for-month", response_model=VehicleServiceMostPopularSchema)
def get_most_popular_service_for_month(number_of_month: Month, year: str):
    """Get the most popular service for a specific month"""
    return VehicleServiceController.get_most_popular_service_for_month(number_of_month, year)


@vehicle_service_router.get("/get-most-popular-service-for-year", response_model=VehicleServiceMostPopularSchema)
def get_most_popular_service_for_year(year: str):
    """Get the most popular service for a specific year"""
    return VehicleServiceController.get_most_popular_service_for_year(year)
