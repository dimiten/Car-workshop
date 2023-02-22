"""Employee schemas"""


from pydantic import BaseModel, UUID4, EmailStr
from typing import Optional


class EmployeeSchema(BaseModel):
    """Employee schema"""
    id: UUID4
    name: str
    surname: str
    email: str
    phone_number: str
    position: str
    is_admin: bool

    class Config:
        orm_mode = True


class EmployeeSchemaWithPassword(BaseModel):
    """Employee with password schema"""
    id: UUID4
    name: str
    surname: str
    email: str
    password: Optional[str]
    phone_number: str
    position: str
    is_admin: bool

    class Config:
        orm_mode = True


class EmployeeSchemaIn(BaseModel):
    """Employee schema in"""
    name: str
    surname: str
    email: EmailStr
    phone_number: str
    position: str

    class Config:
        orm_mode = True


class EmployeeSchemaWithPasswordIn(BaseModel):
    """Employee with password schema in"""
    name: str
    surname: str
    email: EmailStr
    password: str
    phone_number: str
    position: str

    class Config:
        orm_mode = True


class LoginEmployeeSchema(BaseModel):
    """Employee schema for login"""
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
