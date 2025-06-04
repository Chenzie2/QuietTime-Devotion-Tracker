from sqlalchemy import create_engine
from lib.models import Base  

engine = create_engine("sqlite:///quiettime_devotion_tracker.db", echo=False)

Base.metadata.create_all(engine)

print("Database and tables created successfully.")
