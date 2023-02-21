"""Service type controller"""


from app.service_types.services import ServiceTypeServices
from fastapi import HTTPException, Response
from app.service_types.exceptions import ServiceTypeExistsException


class ServiceTypeController:
    """ServiceTypeController class"""

    @staticmethod
    def create_service_type(name: str, cost: float):
        """Creates a service type"""
        try:
            service_type = ServiceTypeServices.create_service_type(name, cost)
            return service_type
        except ServiceTypeExistsException as e:
            raise HTTPException(status_code=e.status_code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_service_type_by_name(name: str):
        """Returns a service type by name"""
        service_type = ServiceTypeServices.get_service_type_by_name(name)
        if service_type:
            return service_type
        raise HTTPException(status_code=400, detail=f"Service type with provided name: {name} does not exist")

    @staticmethod
    def get_all_service_types():
        """Returns all service types"""
        service_types = ServiceTypeServices.get_all_service_types()
        return service_types

    @staticmethod
    def delete_service_type_by_name(name: str):
        """Deletes service type by name"""
        service_type = ServiceTypeServices.get_service_type_by_name(name)
        if service_type:
            ServiceTypeServices.delete_service_type_by_name(name)
            return Response(content=f"Service type with name: {name} is deleted")
        raise HTTPException(status_code=400, detail=f"Service type with provided name: {name} does not exist")

    @staticmethod
    def update_service_type_cost(name: str, cost: float):
        """Updates service type cost"""
        service_type = ServiceTypeServices.get_service_type_by_name(name)
        if service_type:
            return ServiceTypeServices.update_service_type_cost(name, cost)
        raise HTTPException(status_code=400, detail=f"Service type with provided name: {name} does not exist")
