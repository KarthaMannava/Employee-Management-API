from fastapi_crud.models import Employee
from fastapi_crud.schemas import EmployeeCreate
from sqlalchemy.orm import Session
from fastapi_crud.models import Employee
from fastapi_crud.schemas import EmployeeCreate


def create_employee(db: Session, emp: EmployeeCreate):
    employee = Employee(**emp.model_dump())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_employees(db: Session):
    return db.query(Employee).all()

def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()

def delete_employee(db: Session, emp_id: int):
    emp = get_employee(db, emp_id)
    if emp:
        db.delete(emp)
        db.commit()
    return emp
