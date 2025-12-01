from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STORAGE_DIR = directory=str(BASE_DIR / "storage" / "my_db.db")
SQLLITE_DATABASE_URL = f"sqlite:///{STORAGE_DIR}"

engine = create_engine(SQLLITE_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit = False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()