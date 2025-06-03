from models import session, User, Category, DevotionSession, FavoriteVerse
from datetime import datetime

# Clear existing data
session.query(FavoriteVerse).delete()
session.query(DevotionSession).delete()
session.query(Category).delete()
session.query(User).delete()
session.commit()  

# Create users
user1 = User(first_name="Grace", last_name="Wairimu", age=21, gender="Female", email="gracie@gmail.com")
user2 = User(first_name="Dammy", last_name="Olaniyan", age=22, gender="Female", email="dammy@gmail.com")
user3 = User(first_name="Adrian", last_name="Maduafokwa", age=23, gender="Male", email="adrian@gmail.com")
user4 = User(first_name="John", last_name="Kempa", age=26, gender="Male", email="john@gmail.com")

# Create categories
cat1 = Category(name="Prayer")
cat2 = Category(name="Worship")
cat3 = Category(name="Bible Study")
cat4 = Category(name="Sermon")

# Create devotion sessions
session1 = DevotionSession(
    title="Morning Prayer",
    scripture_read="Psalm 23",
    reflection="Felt the Presence of God in the room.",
    date=datetime(2025, 6, 1),
    user=user1,
    category=cat1
)

session2 = DevotionSession(
    title="Evening Worship",
    scripture_read="John 4:24",
    reflection="Listened to First Love Music.",
    date=datetime(2025, 6, 2),
    user=user2,
    category=cat2
)


verse1 = FavoriteVerse(
    verse_text="I can do all things through Christ who strengthens me.",
    book="Philippians",
    chapter=4,
    verse_number=13,
    user=user1
)

verse2 = FavoriteVerse(
    verse_text="The Lord is my shepherd; I shall not want.",
    book="Psalm",
    chapter=23,
    verse_number=1,
    user=user4
)


# Add all objects to session
session.add_all([user1, user2, user3, user4, cat1, cat2, cat3, cat4, session1, session2, verse1, verse2])

# Commit to save 
session.commit()

print("Database seeded successfully.")
