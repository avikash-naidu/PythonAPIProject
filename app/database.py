from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
#tester comment

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

Base = declarative_base()

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#connect to data base
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastAPI', user='postgres', password='anjana99', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('DB connection was successful')
#         break
#     except Exception as error:
#         print('connecting to DB failure')
#         print("Error: " + error)
#         time.sleep(2)
