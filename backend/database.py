
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os


engine = create_engine(
    os.getenv("DATABASE_URL"),
    echo=True
)

# Create base classe => database module
Base = declarative_base()

# Create session maker
Session = sessionmaker()
