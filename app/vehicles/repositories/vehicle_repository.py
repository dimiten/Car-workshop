"""Vehicle repository"""


from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.vehicles.models import Vehicle


class VehicleRepository:
    """VehicleRepository class"""

    def __init__(self, db: Session):
        self.db = db

    def create_vehicle(self, license_plate, manufacturer, model, manufacture_year, customer_id):
        """Create a vehicle"""
        try:
            vehicle = Vehicle(license_plate, manufacturer, model, manufacture_year, customer_id)
            self.db.add(vehicle)
            self.db.commit()
            self.db.refresh(vehicle)
            return vehicle
        except IntegrityError as e:
            raise e

    def get_vehicle_by_id(self, vehicle_id: str):
        """Get a vehicle by id"""
        try:
            vehicle = self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
            return vehicle
        except Exception as e:
            raise e

    def get_all_vehicles(self):
        """Get all vehicles"""
        try:
            vehicles = self.db.query(Vehicle).all()
            return vehicles
        except Exception as e:
            raise e

    def delete_vehicle_by_id(self, vehicle_id: str):
        """Delete a vehicle by id"""
        try:
            vehicle = self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
            self.db.delete(vehicle)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_vehicle(self, vehicle_id: str, license_plate: str = None, manufacturer: str = None, model: str = None,
                       manufacture_year: str = None, customer_id: str = None):
        """Update a vehicle"""
        try:
            vehicle = self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
            if license_plate is not None:
                vehicle.license_plate = license_plate
            if manufacturer is not None:
                vehicle.manufacturer = manufacturer
            if model is not None:
                vehicle.model = model
            if manufacture_year is not None:
                vehicle.manufacture_year = manufacture_year
            if customer_id is not None:
                vehicle.customer_id = customer_id
            self.db.add(vehicle)
            self.db.commit()
            self.db.refresh(vehicle)
            return vehicle
        except Exception as e:
            raise e

    def get_vehicles_license_plates(self):
        """Get all license plates"""
        try:
            license_plates = self.db.query(Vehicle.license_plate).all()
            return [item for t in license_plates for item in t]
        except Exception as e:
            raise e

    def get_all_vehicles_by_manufacture_year(self, manufacture_year: str):
        """Get all vehicles by year of manufacturing"""
        try:
            vehicles = self.db.query(Vehicle).filter(Vehicle.manufacture_year == manufacture_year).all()
            return vehicles
        except Exception as e:
            raise e

    def get_all_vehicles_by_manufacturer(self, manufacturer: str):
        """Get all vehicles by manufacturer"""
        try:
            vehicles = self.db.query(Vehicle).filter(Vehicle.manufacturer == manufacturer).all()
            return vehicles
        except Exception as e:
            raise e

    def get_all_vehicles_by_model(self, manufacturer: str, model: str):
        """Get all vehicles by model"""
        try:
            vehicles = self.db.query(Vehicle).filter(Vehicle.manufacturer == manufacturer, Vehicle.model == model).all()
            return vehicles
        except Exception as e:
            raise e
