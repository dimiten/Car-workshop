"""Vehicle schemas"""


from pydantic import BaseModel, UUID4


class VehicleSchema(BaseModel):
    """Vehicle schema"""
    id: UUID4
    license_plate: str
    manufacturer: str
    model: str
    manufacture_year: str
    customer_id: str

    class Config:
        orm_mode = True


class VehicleSchemaIn(BaseModel):
    """Vehicle schema when creating a vehicle"""
    license_plate: str
    manufacturer: str
    model: str
    manufacture_year: str
    customer_id: str

    class Config:
        orm_mode = True
