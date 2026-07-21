from app.database.database import Base
from app.database.database import engine

# Import all models

from app.database.models import *

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")