from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///quiettime_devotion_tracker.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


from .user import User
from .devotion_session import DevotionSession
from .favorite_verse import FavoriteVerse
from .category import Category


Base.metadata.create_all(engine)


__all__ = ["User", "DevotionSession", "FavoriteVerse", "Category"]
