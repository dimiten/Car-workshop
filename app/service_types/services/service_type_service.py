"""Service type services"""


from app.service_types.repositories import ServiceTypeRepository
from app.db.database import SessionLocal
from app.service_types.exceptions import ServiceTypeExistsException


class ServiceTypeServices:
    """ServiceTypeServices class"""

    @staticmethod
    def create_service_type(name, cost):
        """Creates a service type"""
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                service_type = service_type_repository.get_service_type_by_name(service_type_name=name)
                if service_type is None:
                    return service_type_repository.create_service_type(name, cost)
                raise ServiceTypeExistsException(status_code=400,
                                                 message=f"Service type with name: {name} already exists")
        except Exception as e:
            raise e

    @staticmethod
    def get_service_type_by_name(name: str):
        """Returns a service type by name"""
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.get_service_type_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_service_types():
        """Returns all service types"""
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.get_all_service_types()
        except Exception as e:
            raise e

    @staticmethod
    def delete_service_type_by_name(name: str):
        """Deletes service type by name"""
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.delete_service_type_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def update_service_type_cost(name: str, cost: float):
        """Updates service type cost"""
        try:
            with SessionLocal() as db:
                service_type_repository = ServiceTypeRepository(db)
                return service_type_repository.update_service_type_cost(name, cost)
        except Exception as e:
            raise e
