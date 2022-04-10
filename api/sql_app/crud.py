from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from . import models, schemas

from fastapi import HTTPException

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).one()

def get_customer_by_email(db: Session, email: str):
    return db.query(models.Customer).filter(models.Customer.email == email).first()

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(email=customer.email, first_name=customer.first_name, last_name=customer.last_name)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    c = get_customer(db, customer_id)
    db.delete(c)
    db.commit()
    return c

def update_customer(db: Session, customer: schemas.CustomerCreate):
    c = get_customer(db, customer.id)
    c.email = customer.email
    c.first_name = customer.first_name
    c.last_name = customer.last_name
    db.commit()
    return c


def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).one()

def get_car_by_license_plate(db: Session, license_plate: str):
    return db.query(models.Car).filter(models.Car.license_plate == license_plate).first()

def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Car).offset(skip).limit(limit).all()

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(brand=car.brand, license_plate=car.license_plate)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def delete_car(db: Session, car_id: int):
    c = db.query(models.Car).filter(models.Car.id == car_id).one()
    db.delete(c)
    db.commit()
    return c

def update_car(db: Session, car: schemas.CarCreate):
    c = get_car(db, car.id)
    c.brand = car.brand
    c.license_plate = car.license_plate
    db.commit()
    return c


def sum_driven_km(db: Session, car_id:int):
    return db.query(
            models.Rent.car,
            func.sum(models.Rent.driven_km).label('driven_km')
        ).join(models.Car
        ).filter(models.Rent.car_id == car_id
        ).group_by(models.Rent.car_id
        ).first()


def count_active_rents(db: Session):
    return db.query(models.Rent).filter(
        models.Rent.active_rent == True 
        ).count()

def get_active_car_rent(db: Session, car_id:int):
    return db.query(models.Rent).filter(
        models.Rent.car_id == car_id,
        models.Rent.active_rent == True 
        ).first()

def get_rent(db: Session, rent_id: int):
    return db.query(models.Rent).filter(models.Rent.id == rent_id).one()

def get_rents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rent).offset(skip).limit(limit).all()

def create_rent(db: Session, rent: schemas.RentCreate, customer_id: int, car_id:int):
    r = get_active_car_rent(db, car_id)
    print(r)
    if r != None:
        raise HTTPException(status_code=400, detail="Car is already rented out")
    db_rent = models.Rent(**rent.dict(), customer_id=customer_id, car_id=car_id, driven_km=0, active_rent=True)
    db.add(db_rent)
    db.commit()
    db.refresh(db_rent)
    return db_rent

def end_rent(db: Session, customer_id:int, car_id:int, driven_km:int):
    r = get_active_car_rent(db, car_id)
    if r == None:
        raise HTTPException(status_code=400, detail="Car is not rented out")
    r.driven_km = driven_km
    r.active_rent = False
    db.commit()
    return r

def delete_rent(db: Session, rent_id: int):
    r = db.query(models.Rent).filter(models.Rent.id == rent_id).one()
    db.delete(r)
    db.commit()
    return r




# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_customer_item(db: Session, item: schemas.ItemCreate, customer_id: int):
#     db_item = models.Item(**item.dict(), owner_id=customer_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item