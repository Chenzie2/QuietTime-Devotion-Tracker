from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base

class DevotionSession(Base):
    __tablename__ = 'devotion_sessions'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    scripture_read = Column(Text, nullable=False)
    reflection = Column(Text)

    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    user = relationship("User", back_populates="devotion_sessions")
    category = relationship("Category", back_populates="devotion_sessions")

def __repr__(self):
    return (
        f"<DevotionSession #{self.id}: {self.date.strftime('%Y-%m-%d')} | "
        f"Scripture: {self.scripture_read[:30]}... | User ID: {self.user_id}, Category ID: {self.category_id}>"
    )
