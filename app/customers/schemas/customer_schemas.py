from pydantic import BaseModel, UUID4, EmailStr


class CustomerSchema(BaseModel):
    id: UUID4
    name: str
    surname: str
    email: str
    phone_number: str
    is_regular: bool

    class Config:
        orm_mode = True


class CustomerSchemaIn(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone_number: str

    class Config:
        orm_mode = True
