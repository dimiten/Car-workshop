from datetime import date

from app.vehicle_services.services import VehicleServicesServices
from fastapi import HTTPException, Response
from app.vehicle_services.exceptions import *


class VehicleServiceController:

    @staticmethod
    def create_vehicle_service(date_of_service: date, vehicle_id: str, employee_id: str, service_type_name: str):
        try:
            vehicle_service = VehicleServicesServices.create_vehicle_service(date_of_service, vehicle_id, employee_id,
                                                                             service_type_name)
            return vehicle_service
        except ValueError:
            raise HTTPException(status_code=422, detail="Invalid date format. Must be in YYYY-MM-DD format.")
        except InvalidVehicleException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except InvalidEmployeeException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except InvalidServiceTypeException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_vehicle_service_by_id(vehicle_service_id: str):
        vehicle_service = VehicleServicesServices.get_vehicle_service_by_id(vehicle_service_id)
        if vehicle_service:
            return vehicle_service
        else:
            raise HTTPException(status_code=400,
                                detail=f"Vehicle service with provided id: {vehicle_service_id} does not exist")

    @staticmethod
    def get_all_vehicle_services():
        try:
            vehicle_services = VehicleServicesServices.get_all_vehicle_services()
            return vehicle_services
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_vehicle_service_by_id(vehicle_service_id: str):
        vehicle_service = VehicleServicesServices.get_vehicle_service_by_id(vehicle_service_id)
        if vehicle_service:
            VehicleServicesServices.delete_vehicle_service_by_id(vehicle_service_id)
            return Response(content=f"Vehicle service with id - {vehicle_service_id} is deleted")
        else:
            raise HTTPException(status_code=400,
                                detail=f"Vehicle service with provided id: {vehicle_service_id} does not exist")

    @staticmethod
    def update_vehicle_service(vehicle_service_id: str, date_of_service: str = None, vehicle_id: str = None,
                               employee_id: str = None, service_type_name: str = None):
        vehicle_service = VehicleServicesServices.get_vehicle_service_by_id(vehicle_service_id)
        if vehicle_service:
            return VehicleServicesServices.update_vehicle_service(vehicle_service_id, date_of_service, vehicle_id,
                                                                  employee_id, service_type_name)
        else:
            raise HTTPException(status_code=400,
                                detail=f"Vehicle service with provided id: {vehicle_service_id} does not exist")
