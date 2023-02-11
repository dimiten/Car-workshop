from pydantic import BaseModel, UUID4


class VehicleSchema(BaseModel):
    id: UUID4
    license_plate: str
    manufacturer: str
    model: str
    manufacture_year: str
    customer_id: str

    class Config:
        orm_mode = True


class VehicleSchemaIn(BaseModel):
    license_plate: str
    manufacturer: str
    model: str
    manufacture_year: str
    customer_id: str

    class Config:
        orm_mode = True
