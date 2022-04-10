from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)

    rents = relationship("Rent", back_populates="customer")

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    license_plate = Column(String, unique=True, index=True)

    rents = relationship("Rent", back_populates="car")


class Rent(Base):
    __tablename__ = "rents"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))
    driven_km = Column(Integer, index=True)
    active_rent = Column(Boolean, index=True)

    customer = relationship("Customer", back_populates="rents")
    car = relationship("Car", back_populates="rents")
