import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

db_pwd = os.getenv("db_pwd")

#DB connection : db+driver://username:pwd@localhost:5432/db_name
db_url = f"postgresql+psycopg2://postgres:{db_pwd}@localhost:5432/powerhouse"
engine = create_engine(db_url)
session = sessionmaker(autocommit= False, autoflush= False, bind= engine)

# try:
#     with engine.connect() as connection:
#         print("Database connected successfully!")
# except Exception as e:
#     print("Database connection failed:", e)