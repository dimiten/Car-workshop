"""Service types routes"""


from fastapi import APIRouter, Depends
from app.service_types.controller import ServiceTypeController
from app.service_types.schemas import ServiceTypeSchema
from app.employees.controller import JWTBearer


service_type_router = APIRouter(tags=["Service types"], prefix="/api/service-types")


@service_type_router.post("/add-new-service-type", response_model=ServiceTypeSchema,
                          dependencies=[Depends(JWTBearer("admin"))])
def create_service_type(service_type: ServiceTypeSchema):
    """Creates a service type"""
    return ServiceTypeController.create_service_type(service_type.name, service_type.cost)


@service_type_router.get("/name", response_model=ServiceTypeSchema)
def get_service_type_by_name(name: str):
    """Get service type by name"""
    return ServiceTypeController.get_service_type_by_name(name)


@service_type_router.get("/get-all-service-types", response_model=list[ServiceTypeSchema],
                         dependencies=[Depends(JWTBearer("not admin"))])
def get_all_service_types():
    """Get all service types"""
    return ServiceTypeController.get_all_service_types()


@service_type_router.put("/update/cost", response_model=ServiceTypeSchema)
def update_service_type_cost(name: str, cost: float):
    """Update service type cost"""
    return ServiceTypeController.update_service_type_cost(name, cost)


@service_type_router.delete("/")
def delete_service_type_by_name(name: str):
    """Delete service type by name"""
    return ServiceTypeController.delete_service_type_by_name(name)
