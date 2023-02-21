from fastapi import APIRouter
from app.employees.controller import EmployeeController, JWTBearer
from app.employees.schemas import *

employee_router = APIRouter(tags=["Employees"], prefix="/api/employees")


@employee_router.post("/add-new-employee", response_model=EmployeeSchema)
def create_employee(employee: EmployeeSchemaIn):
    return EmployeeController.create_employee(employee.name, employee.surname, employee.email, employee.phone_number,
                                              employee.position)


@employee_router.post("/add-new-employee-with-password", response_model=EmployeeSchemaWithPassword)
def create_employee_with_password(employee: EmployeeSchemaWithPasswordIn):
    return EmployeeController.create_employee_with_password(employee.name, employee.surname, employee.email,
                                                            employee.phone_number,
                                                            employee.position, employee.password)


@employee_router.post("/login")
def login_employee(employee: LoginEmployeeSchema):
    return EmployeeController.login_employee(employee.email, employee.password)


@employee_router.get("/id", response_model=EmployeeSchema)
def get_employee_by_id(employee_id: str):
    return EmployeeController.get_employee_by_id(employee_id=employee_id)


@employee_router.get("/get-all-employees", response_model=list[EmployeeSchema])
def get_all_employees():
    return EmployeeController.get_all_employees()


@employee_router.put("/update/is_admin", response_model=EmployeeSchema)
def update_employee_is_admin(employee_id: str, is_admin: bool):
    return EmployeeController.update_employee_is_admin(employee_id=employee_id, is_admin=is_admin)


@employee_router.delete("/")
def delete_employee_by_id(employee_id: str):
    return EmployeeController.delete_employee_by_id(employee_id=employee_id)
