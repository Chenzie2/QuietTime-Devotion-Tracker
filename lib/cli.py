from models import session
from models.user import User
from models.category import Category
from models.devotion_session import DevotionSession
from models.favorite_verse import FavoriteVerse

def main_menu():
    while True:
        print("\n--- QuietTime Devotion Tracker ---")
        print("1. Manage Users")
        print("2. Manage Categories")
        print("3. Manage Devotion Sessions")
        print("4. Manage Favorite Verses")
        print("0. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            user_menu()
        elif choice == "2":
            category_menu()
        elif choice == "3":
            devotion_session_menu()
        elif choice == "4":
            favorite_verse_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

#  USER MENU & FUNCTIONS 

def user_menu():
    while True:
        print("\n-- User Menu --")
        print("1. Create User")
        print("2. Delete User")
        print("3. Show All Users")
        print("4. View User's Devotion Sessions")
        print("5. Find User by Email")
        print("0. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            create_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            show_all_users()
        elif choice == "4":
            view_user_devotion_sessions()
        elif choice == "5":
            find_user_by_email()
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")

def create_user():
    print("\n-- Create a New User --")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    email = input("Email: ").strip()
    age_input = input("Age (optional): ").strip()
    gender = input("Gender (optional): ").strip()

    if not first_name or not last_name or not email:
        print("First name, last name, and email are required.")
        return

    age = None
    if age_input:
        if age_input.isdigit():
            age = int(age_input)
        else:
            print("Invalid age; must be a number.")
            return

    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        print("User with that email already exists.")
        return

    new_user = User(first_name=first_name, last_name=last_name, email=email, age=age, gender=gender)
    session.add(new_user)
    session.commit()
    print(f"User {first_name} {last_name} created successfully!")

def delete_user():
    email = input("Enter the email of the user to delete: ").strip()
    user = session.query(User).filter_by(email=email).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user.first_name} {user.last_name} deleted.")
    else:
        print("User not found.")

def show_all_users():
    users = session.query(User).all()
    if not users:
        print("No users found.")
        return
    print("\nAll Users:")
    for u in users:
        print(f"ID: {u.id}, Name: {u.first_name} {u.last_name}, Email: {u.email}, Age: {u.age}, Gender: {u.gender}")

def view_user_devotion_sessions():
    email = input("Enter the user's email: ").strip()
    user = session.query(User).filter_by(email=email).first()
    if user:
        sessions = user.devotion_sessions
        if not sessions:
            print("No devotion sessions found for this user.")
            return
        print(f"\nDevotion Sessions for {user.first_name} {user.last_name}:")
        for s in sessions:
            print(f"ID: {s.id}, Date: {s.date}, Scripture: {s.scripture_read}, Reflection: {s.reflection}")
    else:
        print("User not found.")

def find_user_by_email():
    email = input("Enter email to search: ").strip()
    user = session.query(User).filter_by(email=email).first()
    if user:
        print(f"User found: {user.first_name} {user.last_name}, Age: {user.age}, Gender: {user.gender}")
    else:
        print("User not found.")

# CATEGORY MENU & FUNCTIONS 

def category_menu():
    while True:
        print("\n-- Category Menu --")
        print("1. Create Category")
        print("2. Delete Category")
        print("3. Show All Categories")
        print("4. View Devotion Sessions by Category")
        print("5. Find Category by Name")
        print("0. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            create_category()
        elif choice == "2":
            delete_category()
        elif choice == "3":
            show_all_categories()
        elif choice == "4":
            view_devotion_sessions_by_category()
        elif choice == "5":
            find_category_by_name()
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")

def create_category():
    name = input("Category Name: ").strip()
    if not name:
        print("Category name cannot be empty.")
        return
    existing = session.query(Category).filter_by(name=name).first()
    if existing:
        print("Category already exists.")
        return
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' created.")

def delete_category():
    name = input("Enter category name to delete: ").strip()
    category = session.query(Category).filter_by(name=name).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category '{name}' deleted.")
    else:
        print("Category not found.")

def show_all_categories():
    categories = session.query(Category).all()
    if not categories:
        print("No categories found.")
        return
    print("\nCategories:")
    for c in categories:
        print(f"ID: {c.id}, Name: {c.name}")

def view_devotion_sessions_by_category():
    name = input("Enter category name: ").strip()
    category = session.query(Category).filter_by(name=name).first()
    if category:
        sessions = category.devotion_sessions
        if not sessions:
            print("No devotion sessions found in this category.")
            return
        print(f"\nDevotion Sessions in category '{name}':")
        for s in sessions:
            print(f"ID: {s.id}, Date: {s.date}, Scripture: {s.scripture_read}, Reflection: {s.reflection}")
    else:
        print("Category not found.")

def find_category_by_name():
    name = input("Enter category name to search: ").strip()
    category = session.query(Category).filter_by(name=name).first()
    if category:
        print(f"Category found: ID {category.id}, Name: {category.name}")
    else:
        print("Category not found.")

#  DEVOTION SESSION MENU & FUNCTIONS 

def devotion_session_menu():
    while True:
        print("\n-- Devotion Session Menu --")
        print("1. Create Devotion Session")
        print("2. Delete Devotion Session")
        print("3. Show All Devotion Sessions")
        print("4. View Favorite Verses for a Devotion Session (N/A)")  # Not linked, so placeholder
        print("5. Find Devotion Session by Date")
        print("0. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            create_devotion_session()
        elif choice == "2":
            delete_devotion_session()
        elif choice == "3":
            show_all_devotion_sessions()
        elif choice == "4":
            print("Not implemented: favorite verses are linked to users, not devotion sessions.")
        elif choice == "5":
            find_devotion_session_by_date()
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")

def create_devotion_session():
    print("\n-- Create Devotion Session --")
    email = input("User's Email: ").strip()
    user = session.query(User).filter_by(email=email).first()
    if not user:
        print("User not found.")
        return

    date_input = input("Date (YYYY-MM-DD HH:MM:SS) or leave empty for now: ").strip()
    from datetime import datetime
    date = None
    if date_input:
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid datetime format. Use YYYY-MM-DD HH:MM:SS")
            return

    scripture_read = input("Scripture Read: ").strip()
    reflection = input("Reflection: ").strip()

    print("Available Categories:")
    categories = session.query(Category).all()
    for c in categories:
        print(f"- {c.name}")

    category_name = input("Category name: ").strip()
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        print("Category not found.")
        return

    new_session = DevotionSession(date=date, scripture_read=scripture_read, reflection=reflection,
                                  user_id=user.id, category_id=category.id)
    session.add(new_session)
    session.commit()
    print("Devotion session created successfully!")

def delete_devotion_session():
    session_id = input("Enter devotion session ID to delete: ").strip()
    if not session_id.isdigit():
        print("Invalid ID.")
        return
    ds = session.query(DevotionSession).filter_by(id=int(session_id)).first()
    if ds:
        session.delete(ds)
        session.commit()
        print("Devotion session deleted.")
    else:
        print("Devotion session not found.")

def show_all_devotion_sessions():
    sessions = session.query(DevotionSession).all()
    if not sessions:
        print("No devotion sessions found.")
        return
    print("\nAll Devotion Sessions:")
    for s in sessions:
        user = session.query(User).filter_by(id=s.user_id).first()
        category = session.query(Category).filter_by(id=s.category_id).first()
        print(f"ID: {s.id}, Date: {s.date}, User: {user.first_name} {user.last_name}, "
              f"Category: {category.name}, Scripture: {s.scripture_read}, Reflection: {s.reflection}")

def find_devotion_session_by_date():
    date_input = input("Enter date (YYYY-MM-DD): ").strip()
    from datetime import datetime
    try:
        date = datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return
    sessions = session.query(DevotionSession).filter(
        DevotionSession.date != None,
        DevotionSession.date.cast("date") == date
    ).all()
    if not sessions:
        print("No devotion sessions found for that date.")
        return
    print(f"\nDevotion sessions on {date_input}:")
    for s in sessions:
        print(f"ID: {s.id}, Scripture: {s.scripture_read}, Reflection: {s.reflection}")

# FAVORITE VERSE MENU & FUNCTIONS 

def favorite_verse_menu():
    while True:
        print("\n-- Favorite Verse Menu --")
        print("1. Add Favorite Verse")
        print("2. Delete Favorite Verse")
        print("3. Show All Favorite Verses")
        print("4. View User's Favorite Verses")
        print("0. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_favorite_verse()
        elif choice == "2":
            delete_favorite_verse()
        elif choice == "3":
            show_all_favorite_verses()
        elif choice == "4":
            view_user_favorite_verses()
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")

def add_favorite_verse():
    print("\n-- Add Favorite Verse --")
    email = input("User's Email: ").strip()
    user = session.query(User).filter_by(email=email).first()
    if not user:
        print("User not found.")
        return

    verse_text = input("Verse Text: ").strip()
    book = input("Book: ").strip()
    chapter_input = input("Chapter (number): ").strip()
    verse_number_input = input("Verse Number: ").strip()

    if not chapter_input.isdigit() or not verse_number_input.isdigit():
        print("Chapter and verse number must be numbers.")
        return

    chapter = int(chapter_input)
    verse_number = int(verse_number_input)

    fav = FavoriteVerse(verse_text=verse_text, book=book, chapter=chapter,
                        verse_number=verse_number, user_id=user.id)
    session.add(fav)
    session.commit()
    print("Favorite verse added.")

def delete_favorite_verse():
    verse_id = input("Enter favorite verse ID to delete: ").strip()
    if not verse_id.isdigit():
        print("Invalid ID.")
        return
    fv = session.query(FavoriteVerse).filter_by(id=int(verse_id)).first()
    if fv:
        session.delete(fv)
        session.commit()
        print("Favorite verse deleted.")
    else:
        print("Favorite verse not found.")

def show_all_favorite_verses():
    verses = session.query(FavoriteVerse).all()
    if not verses:
        print("No favorite verses found.")
        return
    print("\nAll Favorite Verses:")
    for v in verses:
        user = session.query(User).filter_by(id=v.user_id).first()
        print(f"ID: {v.id}, Verse: {v.verse_text} ({v.book} {v.chapter}:{v.verse_number}), User: {user.first_name} {user.last_name}")

def view_user_favorite_verses():
    email = input("Enter user email: ").strip()
    user = session.query(User).filter_by(email=email).first()
    if not user:
        print("User not found.")
        return
    verses = user.favorite_verses
    if not verses:
        print("No favorite verses found for this user.")
        return
    print(f"\nFavorite Verses for {user.first_name} {user.last_name}:")
    for v in verses:
        print(f"ID: {v.id}, Verse: {v.verse_text} ({v.book} {v.chapter}:{v.verse_number})")



if __name__ == "__main__":
    main_menu()
