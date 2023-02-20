from pydantic import BaseModel, UUID4, EmailStr
from datetime import date


class CustomerSchema(BaseModel):
    id: UUID4
    name: str
    surname: str
    email: str
    phone_number: str
    date_of_registration: date
    is_regular: bool

    class Config:
        orm_mode = True


class CustomerSchemaIn(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone_number: str
    date_of_registration: date

    class Config:
        orm_mode = True


class NumberNewCustomersSchema(BaseModel):
    number_of_new_customers: int

    class Config:
        orm_mode = True
