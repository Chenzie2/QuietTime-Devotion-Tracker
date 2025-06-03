from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///devotion_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
