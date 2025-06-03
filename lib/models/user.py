from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base

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

    def __repr__(self):
        return (
        f"<DevotionSession #{self.id}: {self.date.strftime('%Y-%m-%d')} | "
        f"Scripture: {self.scripture_read[:30]}... | User ID: {self.user_id}, Category ID: {self.category_id}>"
    )
