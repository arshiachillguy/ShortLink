from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQlALCHEMY_DATABASE_URL = "postgresql://postgres:arshiapsq@localhost:5432/shortlink"

engine = create_engine(SQlALCHEMY_DATABASE_URL , echo=True)

SessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()










