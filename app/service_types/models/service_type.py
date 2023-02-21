"""Service type model"""


from app.db.database import Base
from sqlalchemy import Column, String, Float


class ServiceType(Base):
    """ServiceType class"""
    __tablename__ = "service_types"
    name = Column(String(50), primary_key=True, autoincrement=False)
    cost = Column(Float)

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
