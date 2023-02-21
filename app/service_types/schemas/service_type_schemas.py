"""Service type schemas"""


from pydantic import BaseModel


class ServiceTypeSchema(BaseModel):
    """Service type schema"""
    name: str
    cost: float

    class Config:
        orm_mode = True
