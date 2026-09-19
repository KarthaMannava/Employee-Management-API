from fastapi_crud.database import Base
from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from sqlalchemy.sql import func
from fastapi_crud.database import Base

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String)
    salary = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default=func.now())
