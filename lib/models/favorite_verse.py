from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class FavoriteVerse(Base):
    __tablename__ = 'favorite_verses'

    id = Column(Integer, primary_key=True)
    verse_text = Column(Text, nullable=False)
    book = Column(String, nullable=False)
    chapter = Column(Integer, nullable=False)
    verse_number = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="favorite_verses")

def __repr__(self):
    return (
        f"<FavoriteVerse #{self.id}: {self.book} {self.chapter}:{self.verse_number} | "
        f"Text: {self.verse_text[:30]}... | User ID: {self.user_id}>"
    )
