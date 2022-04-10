from pydantic import BaseModel
from typing import Optional

class RentBase(BaseModel):
    pass
class RentCreate(RentBase):
    pass

class Rent(RentBase):
    id: int
    customer_id: int
    car_id: int
    driven_km: int
    active_rent: bool

    class Config:
        orm_mode = True

class CarBase(BaseModel):
    brand: str
    license_plate: str

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int
    rents: list[Rent] = []

    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    email: str
    first_name: str
    last_name: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    rents: list[Rent] = []
    cars: list[Car] = []

    class Config:
        orm_mode = True