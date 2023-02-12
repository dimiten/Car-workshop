from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Date
from uuid import uuid4


class VehicleService(Base):
    __tablename__ = "vehicle_services"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    date_of_service = Column(Date)

    vehicle_id = Column(String(50), ForeignKey("vehicles.id"))
    employee_id = Column(String(50), ForeignKey("employees.id"))
    service_type_name = Column(String(50), ForeignKey("service_types.name"))

    def __init__(self, date_of_service, vehicle_id, employee_id, service_type_name):
        self.date_of_service = date_of_service
        self.vehicle_id = vehicle_id
        self.employee_id = employee_id
        self.service_type_name = service_type_name
