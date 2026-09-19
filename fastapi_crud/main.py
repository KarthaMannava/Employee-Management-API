from fastapi_crud.database import SessionLocal, engine
from fastapi_crud import models, schemas, crud
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_crud.database import SessionLocal, engine
from fastapi_crud import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee CRUD API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)

@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.delete_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}
