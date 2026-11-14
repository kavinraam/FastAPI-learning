from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#DB connection
db_url = "postgresql+psycopg2://postgres:1234567@localhost:5432/powerhouse"
engine = create_engine(db_url)
session = sessionmaker(autocommit= False, autoflush= False, bind= engine)

try:
    with engine.connect() as connection:
        print("Database connected successfully!")
except Exception as e:
    print("Database connection failed:", e)