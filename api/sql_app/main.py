from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Customers
@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_email(db, email=customer.email)
    if db_customer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_customer(db=db, customer=customer)


@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers


@app.get("/customer/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@app.delete("/customer/{customer_id}", response_model=schemas.Customer)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return crud.delete_customer(db=db, customer_id=customer_id)

# Cars
@app.post("/cars/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = crud.get_car_by_license_plate(db, license_plate=car.license_plate)
    if db_car:
        raise HTTPException(status_code=400, detail="License plate already registered")
    return crud.create_car(db=db, car=car)


@app.get("/cars/", response_model=list[schemas.Car])
def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cars = crud.get_cars(db, skip=skip, limit=limit)
    return cars

@app.get("/car/{car_id}", response_model=schemas.Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@app.delete("/car/{car_id}", response_model=schemas.Car)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    return crud.delete_car(db=db, car_id=car_id)

# Rents
@app.get("/rents/", response_model=list[schemas.Rent])
def read_rents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rents = crud.get_rents(db, skip=skip, limit=limit)
    return rents

@app.get("/rent/{rent_id}", response_model=schemas.Rent)
def read_rent(rent_id: int, db: Session = Depends(get_db)):
    rents = crud.get_rens(db=db,  rent_id=rent_id)
    return rents

@app.post("/rent/{customer_id}/{car_id}/", response_model=schemas.Rent)
def create_rent(
    customer_id: int, car_id: int, rent: schemas.RentCreate, db: Session = Depends(get_db)
):
    
    return crud.create_rent(db=db, rent=rent, customer_id=customer_id, car_id=car_id)

@app.patch("/rent/{customer_id}/{car_id}/end", response_model=schemas.Rent)
def end_rent(
    customer_id: int, car_id: int, driven_km: int, db: Session = Depends(get_db)
):
    return crud.end_rent(db=db, driven_km=driven_km, customer_id=customer_id, car_id=car_id)

@app.delete("/rent/{rent_id}", response_model=schemas.Rent)
def delete_rent(rent_id: int, db: Session = Depends(get_db)):
    return crud.delete_rent(db=db, rent_id=rent_id)

# Special
@app.get("/rents/count", response_model=int)
def count_active_rents(db: Session = Depends(get_db)):
    return crud.count_active_rents(db=db)

@app.get("/driven_km/{car_id}", response_model=int)
def count_active_rents(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    
    x = crud.sum_driven_km(db=db, car_id=car_id)
    if x is None:
        return 0
    return x.driven_km
    