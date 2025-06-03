from models import session
from models.user import User
from models.devotion_session import DevotionSession
from models.category import Category
from models.favorite_verse import FavoriteVerse

def main_menu():
    while True:
        print("\n--- QuietTime Devotion Tracker ---")
        print("1. Manage Users")
        print("2. Manage Categories")
        print("3. Manage Devotion Sessions")
        print("4. Manage Favorite Verses")
        print("0. Exit")

        actions = {
            "1": user_menu,
            "2": category_menu,
            "3": devotion_session_menu,
            "4": favorite_verse_menu,
            "0": exit_program
        }
        action = actions.get(input("Select an option: ").strip())
        if action:
            action()
        else:
            print("Invalid choice, please try again.")

def exit_program():
    print("Goodbye!")
    exit()

# ----------------- USER MENU -----------------
def user_menu():
    while True:
        print("\n-- User Menu --")
        print("1. Create User")
        print("2. Delete User")
        print("3. Show All Users")
        print("4. View User's Devotion Sessions")
        print("5. Find User by Email")
        print("0. Back to Main Menu")

        actions = {
            "1": create_user,
            "2": delete_user,
            "3": show_all_users,
            "4": view_user_devotion_sessions,
            "5": find_user_by_email,
            "0": lambda: None
        }
        choice = input("Select an option: ").strip()
        if choice == "0":
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")

def create_user():
    print("\n-- Create a New User --")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    email = input("Email: ").strip()
    age_input = input("Age (optional): ").strip()

    gender_options = ('Male', 'Female', 'Other', '')
    gender = input("Gender (Male/Female/Other): ").strip().capitalize()
    if gender not in gender_options:
        print("Invalid gender option.")
        return

    if not first_name or not last_name or not email:
        print("First name, last name, and email are required.")
        return

    age = int(age_input) if age_input.isdigit() else None

    if session.query(User).filter_by(email=email).first():
        print("User with that email already exists.")
        return

    new_user = User(first_name=first_name, last_name=last_name, email=email, age=age, gender=gender)
    try:
        session.add(new_user)
        session.commit()
        print(f"User {new_user.full_name} created successfully!")
    except Exception as e:
        session.rollback()
        print("Error creating user:", e)

def delete_user():
    email = input("Enter the email of the user to delete: ").strip()
    user = session.query(User).filter_by(email=email).first()
    if user:
        try:
            session.delete(user)
            session.commit()
            print(f"User {user.full_name} deleted.")
        except Exception as e:
            session.rollback()
            print("Error deleting user:", e)
    else:
        print("User not found.")

def show_all_users():
    users = session.query(User).all()
    if not users:
        print("No users found.")
        return
    for u in users:
        print(f"ID: {u.id}, Name: {u.full_name}, Email: {u.email}, Age: {u.age}, Gender: {u.gender}")

def view_user_devotion_sessions():
    email = input("Enter the user's email: ").strip()
    user = session.query(User).filter_by(email=email).first()
    if user:
        if not user.devotion_sessions:
            print("No devotion sessions for this user.")
            return
        for s in user.devotion_sessions:
            print(f"ID: {s.id}, Date: {s.date}, Scripture: {s.scripture_read}, Reflection: {s.reflection}")
    else:
        print("User not found.")

def find_user_by_email():
    email = input("Enter email to search: ").strip()
    user = session.query(User).filter_by(email=email).first()
    if user:
        print(f"{user.full_name} - Age: {user.age}, Gender: {user.gender}")
    else:
        print("User not found.")

# ----------------- CATEGORY MENU -----------------
def category_menu():
    while True:
        print("\n-- Category Menu --")
        print("1. Create Category")
        print("2. Delete Category")
        print("3. Show All Categories")
        print("0. Back to Main Menu")

        actions = {
            "1": create_category,
            "2": delete_category,
            "3": show_all_categories,
            "0": lambda: None
        }
        choice = input("Select an option: ").strip()
        if choice == "0":
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")

def create_category():
    name = input("Category name: ").strip()
    if not name:
        print("Category name cannot be empty.")
        return
    if session.query(Category).filter_by(name=name).first():
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
        print("No categories available.")
        return
    for c in categories:
        print(f"ID: {c.id}, Name: {c.name}")

# ----------------- DEVOTION SESSION MENU -----------------
def devotion_session_menu():
    while True:
        print("\n-- Devotion Session Menu --")
        print("1. Create Devotion Session")
        print("2. Delete Devotion Session")
        print("3. Show All Devotion Sessions")
        print("0. Back to Main Menu")

        actions = {
            "1": create_devotion_session,
            "2": delete_devotion_session,
            "3": show_all_devotion_sessions,
            "0": lambda: None
        }
        choice = input("Select an option: ").strip()
        if choice == "0":
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")

def create_devotion_session():
    user_email = input("User email: ").strip()
    user = session.query(User).filter_by(email=user_email).first()
    if not user:
        print("User not found.")
        return

    category_name = input("Category name: ").strip()
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        print("Category not found.")
        return

    scripture = input("Scripture Read: ").strip()
    reflection = input("Reflection: ").strip()

    new_session = DevotionSession(user_id=user.id, category_id=category.id,
                                  scripture_read=scripture, reflection=reflection)
    session.add(new_session)
    session.commit()
    print("Devotion session added.")

def delete_devotion_session():
    session_id = input("Enter Devotion Session ID to delete: ").strip()
    session_obj = session.query(DevotionSession).filter_by(id=session_id).first()
    if session_obj:
        session.delete(session_obj)
        session.commit()
        print("Devotion session deleted.")
    else:
        print("Devotion session not found.")

def show_all_devotion_sessions():
    sessions_list = session.query(DevotionSession).all()
    if not sessions_list:
        print("No devotion sessions found.")
        return
    for s in sessions_list:
        print(f"ID: {s.id}, User: {s.user.full_name}, Category: {s.category.name}, Scripture: {s.scripture_read}, Reflection: {s.reflection}")

# ----------------- FAVORITE VERSE MENU -----------------
def favorite_verse_menu():
    while True:
        print("\n-- Favorite Verse Menu --")
        print("1. Add Favorite Verse")
        print("2. Remove Favorite Verse")
        print("3. Show All Favorite Verses")
        print("0. Back to Main Menu")

        actions = {
            "1": add_favorite_verse,
            "2": remove_favorite_verse,
            "3": show_all_favorite_verses,
            "0": lambda: None
        }
        choice = input("Select an option: ").strip()
        if choice == "0":
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")

def add_favorite_verse():
    user_email = input("User email: ").strip()
    user = session.query(User).filter_by(email=user_email).first()
    if not user:
        print("User not found.")
        return
    verse = input("Enter favorite verse: ").strip()
    if not verse:
        print("Verse cannot be empty.")
        return
    fav = FavoriteVerse(user_id=user.id, verse_text=verse)
    session.add(fav)
    session.commit()
    print("Favorite verse added.")

def remove_favorite_verse():
    verse_id = input("Enter Favorite Verse ID to delete: ").strip()
    fv = session.query(FavoriteVerse).filter_by(id=verse_id).first()
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
    for v in verses:
        print(f"ID: {v.id}, User: {v.user.full_name}, Verse: {v.verse_text}")


if __name__ == "__main__":
    main_menu()