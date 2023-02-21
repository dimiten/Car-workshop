"""Vehicle services schemas"""


from datetime import date
from pydantic import BaseModel, UUID4


class VehicleServiceSchema(BaseModel):
    """Vehicle service schema"""
    id: UUID4
    date_of_service: date
    vehicle_id: str
    employee_id: str
    service_type_name: str

    class Config:
        orm_mode = True


class VehicleServiceSchemaIn(BaseModel):
    """Vehicle service schema for creating vehicle service"""
    date_of_service: date
    vehicle_id: str
    employee_id: str
    service_type_name: str

    class Config:
        orm_mode = True


class VehicleServiceCountSchema(BaseModel):
    """Vehicle service schema for counting number of services"""
    service_type_name: str
    number_of_services: int

    class Config:
        orm_mode = True


class VehicleServiceMonthIncomeSchema(BaseModel):
    """Vehicle service schema for monthly income"""
    income_for_month: float

    class Config:
        orm_mode = True


class VehicleServiceYearIncomeSchema(BaseModel):
    """Vehicle service schema for yearly income"""
    income_for_year: float

    class Config:
        orm_mode = True


class VehicleServiceMostPopularSchema(BaseModel):
    """Vehicle service schema for most popular vehicle service"""
    service_type_name: str
    number_of_services: int

    class Config:
        orm_mode = True
