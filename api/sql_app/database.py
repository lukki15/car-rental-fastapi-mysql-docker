from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

host = os.getenv("DATABASE_HOST")
port = 3306
customer = os.environ.get("DATABASE_USERNAME")
password = os.environ.get("DATABASE_PASSWORD")
database = os.environ.get("DATABASE")

SQLALCHEMY_DATABASE_URL = f"mysql://{customer}:{password}@{host}:{port}/{database}"
# SQLALCHEMY_DATABASE_URL = "postgresql://customer:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()