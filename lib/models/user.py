from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    email = Column(String, unique=True, nullable=False)

    # Relationships
    devotion_sessions = relationship("DevotionSession", back_populates="user")
    favorite_verses = relationship("FavoriteVerse", back_populates="user")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return (
            f"<User #{self.id}: {self.full_name} | "
            f"Email: {self.email} | Age: {self.age} | Gender: {self.gender}>"
        )
