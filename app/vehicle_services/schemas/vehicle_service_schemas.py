from datetime import date

from pydantic import BaseModel, UUID4


class VehicleServiceSchema(BaseModel):
    id: UUID4
    date_of_service: date
    vehicle_id: str
    employee_id: str
    service_type_name: str

    class Config:
        orm_mode = True


class VehicleServiceSchemaIn(BaseModel):
    date_of_service: date
    vehicle_id: str
    employee_id: str
    service_type_name: str

    class Config:
        orm_mode = True
