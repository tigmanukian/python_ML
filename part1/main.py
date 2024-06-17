from typing import List

from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from . import crud
import models
import schemas
from .database import SessionLocal, engine
import requests
import shutil

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/new", response_model=schemas.Employee)
async def create_employee(
    first_name: str,
    last_name: str,
    age: int,
    position: str,
    remote: bool,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Save the uploaded file locally
    with open(f"temp/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Send the image to Service 2 for OCR processing
    with open(f"temp/{file.filename}", "rb") as image:
        response = requests.post("http://localhost:9000/image", files={"file": image})

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error  image")

    employee_id = response.json().get("employee_id")

    employee = schemas.EmployeeCreate(
        first_name=first_name,
        last_name=last_name,
        age=age,
        position=position,
        remote=remote,
        employee_id=employee_id
    )
    return crud.create_employee(db=db, employee=employee)

@app.get("/employees/list", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees

@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


