from pydantic import BaseModel


class ServiceTypeSchema(BaseModel):
    name: str
    cost: float

    class Config:
        orm_mode = True
