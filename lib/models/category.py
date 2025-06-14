from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    devotion_sessions = relationship("DevotionSession", back_populates="category")

    def __repr__(self):
        return f"<Category #{self.id}: {self.name}>"
