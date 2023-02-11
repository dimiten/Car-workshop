from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4


class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    license_plate = Column(String(50), unique=True)
    manufacturer = Column(String(50))
    model = Column(String(50))
    manufacture_year = Column(String(4))

    customer_id = Column(String(50), ForeignKey("customers.id"))

    def __init__(self, license_plate, manufacturer, model, manufacture_year, customer_id):
        self.license_plate = license_plate
        self.manufacturer = manufacturer
        self.model = model
        self.manufacture_year = manufacture_year
        self.customer_id = customer_id
