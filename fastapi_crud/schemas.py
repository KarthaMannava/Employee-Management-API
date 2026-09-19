from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    email: str
    role: str
    salary: float

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True
