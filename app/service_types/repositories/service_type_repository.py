"""Service type repository"""


from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.service_types.models import ServiceType


class ServiceTypeRepository:
    """ServiceTypeRepository class"""

    def __init__(self, db: Session):
        self.db = db

    def create_service_type(self, name, cost):
        """Creates a service type"""
        try:
            service_type = ServiceType(name, cost)
            self.db.add(service_type)
            self.db.commit()
            self.db.refresh(service_type)
            return service_type
        except IntegrityError as e:
            raise e

    def get_service_type_by_name(self, service_type_name: str):
        """Returns a service type by name"""
        try:
            service_type = self.db.query(ServiceType).filter(ServiceType.name == service_type_name).first()
            return service_type
        except Exception as e:
            raise e

    def get_all_service_types(self):
        """Returns all service types"""
        try:
            service_types = self.db.query(ServiceType).all()
            return service_types
        except Exception as e:
            raise e

    def delete_service_type_by_name(self, service_type_name: str):
        """Deletes service type by name"""
        try:
            service_type = self.db.query(ServiceType).filter(ServiceType.name == service_type_name).first()
            self.db.delete(service_type)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_service_type_cost(self, service_type_name: str, service_type_cost: float):
        """Updates service type cost"""
        try:
            service_type = self.db.query(ServiceType).filter(ServiceType.name == service_type_name).first()
            service_type.cost = service_type_cost
            self.db.add(service_type)
            self.db.commit()
            self.db.refresh(service_type)
            return service_type
        except Exception as e:
            raise e
