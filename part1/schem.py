from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    position: str
    remote: bool
    employee_id: str

class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    position: str
    remote: bool
    employee_id: str

    class Config:
        orm_mode = True
