from app.service_types.services import ServiceTypeServices
from fastapi import HTTPException, Response
from app.service_types.exceptions import ServiceTypeExistsException


class ServiceTypeController:

    @staticmethod
    def create_service_type(name: str, cost: float):
        try:
            service_type = ServiceTypeServices.create_service_type(name, cost)
            return service_type
        except ServiceTypeExistsException as e:
            raise HTTPException(status_code=e.status_code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_service_type_by_name(name: str):
        service_type = ServiceTypeServices.get_service_type_by_name(name)
        if service_type:
            return service_type
        else:
            raise HTTPException(status_code=400, detail=f"Service type with provided name: {name} does not exist")

    @staticmethod
    def get_all_service_types():
        service_types = ServiceTypeServices.get_all_service_types()
        return service_types

    @staticmethod
    def delete_service_type_by_name(name: str):
        service_type = ServiceTypeServices.get_service_type_by_name(name)
        if service_type:
            ServiceTypeServices.delete_service_type_by_name(name)
            return Response(content=f"Service type with name: {name} is deleted")
        else:
            raise HTTPException(status_code=400, detail=f"Service type with provided name: {name} does not exist")

    @staticmethod
    def update_service_type_cost(name: str, cost: float):
        service_type = ServiceTypeServices.get_service_type_by_name(name)
        if service_type:
            return ServiceTypeServices.update_service_type_cost(name, cost)
        else:
            raise HTTPException(status_code=400, detail=f"Service type with provided name: {name} does not exist")
