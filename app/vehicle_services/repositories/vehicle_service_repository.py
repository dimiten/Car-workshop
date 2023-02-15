from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.vehicle_services.models import VehicleService


class VehicleServiceRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_vehicle_service(self, date_of_service: date, vehicle_id: str, employee_id: str, service_type_name: str):
        try:
            vehicle_service = VehicleService(date_of_service, vehicle_id, employee_id, service_type_name)
            self.db.add(vehicle_service)
            self.db.commit()
            self.db.refresh(vehicle_service)
            return vehicle_service
        except IntegrityError as e:
            raise e

    def get_vehicle_service_by_id(self, vehicle_service_id: str):
        try:
            vehicle_service = self.db.query(VehicleService).filter(VehicleService.id == vehicle_service_id).first()
            return vehicle_service
        except Exception as e:
            raise e

    def get_all_vehicle_services(self):
        try:
            vehicle_services = self.db.query(VehicleService).all()
            return vehicle_services
        except Exception as e:
            raise e

    def delete_vehicle_service_by_id(self, vehicle_service_id: str):
        try:
            vehicle_service = self.db.query(VehicleService).filter(VehicleService.id == vehicle_service_id).first()
            self.db.delete(vehicle_service)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_vehicle_service(self, vehicle_service_id: str, date_of_service: str = None, vehicle_id: str = None,
                               employee_id: str = None, service_type_name: str = None):
        try:
            vehicle_service = self.db.query(VehicleService).filter(VehicleService.id == vehicle_service_id).first()
            if date_of_service is not None:
                vehicle_service.date_of_service = date_of_service
            if vehicle_id is not None:
                vehicle_service.vehicle_id = vehicle_id
            if employee_id is not None:
                vehicle_service.employee_id = employee_id
            if service_type_name is not None:
                vehicle_service.service_type_name = service_type_name
            self.db.add(vehicle_service)
            self.db.commit()
            self.db.refresh(vehicle_service)
            return vehicle_service
        except Exception as e:
            raise e

    def get_number_of_services_for_month(self, number_of_month: str):
        try:
            number_of_services = self.db.query(VehicleService).filter(
                VehicleService.date_of_service.like(f"%-{number_of_month}-%")).count()
            return number_of_services
        except Exception as e:
            raise e
