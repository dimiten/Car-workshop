from fastapi import APIRouter
from app.service_types.controller import ServiceTypeController
from app.service_types.schemas import ServiceTypeSchema


service_type_router = APIRouter(tags=["Service types"], prefix="/api/service-types")


@service_type_router.post("/add-new-service-type", response_model=ServiceTypeSchema)
def create_service_type(service_type: ServiceTypeSchema):
    return ServiceTypeController.create_service_type(service_type.name, service_type.cost)


@service_type_router.get("/name", response_model=ServiceTypeSchema)
def get_service_type_by_name(name: str):
    return ServiceTypeController.get_service_type_by_name(name)


@service_type_router.get("/get-all-service-types", response_model=list[ServiceTypeSchema])
def get_all_service_types():
    return ServiceTypeController.get_all_service_types()


@service_type_router.put("/update/cost", response_model=ServiceTypeSchema)
def update_service_type_cost(name: str, cost: float):
    return ServiceTypeController.update_service_type_cost(name, cost)


@service_type_router.delete("/")
def delete_service_type_by_name(name: str):
    return ServiceTypeController.delete_service_type_by_name(name)
