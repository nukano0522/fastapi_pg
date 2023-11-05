from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

USER = os.environ['POSTGRES_USER']
PASSWORD = os.environ['POSTGRES_PASSWORD']
DB = os.environ['POSTGRES_DB']
SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@fastapi_psql_postgres_1:5432/{DB}"

print(f"URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
