
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/pizza_delivery',
    echo=True
)

# Create base classe => database module
Base = declarative_base()

# Create session maker
Session = sessionmaker()
