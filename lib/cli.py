from models import session
from models.user import User
from models.devotion_session import DevotionSession
from models.category import Category
from models.favorite_verse import FavoriteVerse



def main_menu():
    while True:
        print("\n===================================================")
        print("    Welcome to your QuietTime Devotion Tracker ")
        print("   Deepen your walk with God, one session at a time")
        print("===================================================")
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
    print("\n--------------------------------------------------")
    print("Thank you for spending time with God today.")
    print("“Draw near to God, and He will draw near to you.” – James 4:8")
    print("Come back soon for another quiet time.")
    print("--------------------------------------------------")
    exit()


# ----------------- USER MENU -----------------
def user_menu():
    while True:
        print("\n----------- USER MENU -----------")
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
            print("Invalid choice, please try again.")

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
        print("\n--------------------------------------------------")
        print(f"Success! User '{new_user.full_name}' was created.")
        print("You're doing great—keep seeking Him daily.")
        print("--------------------------------------------------")
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
            print("\n--------------------------------------------------")
            print(f"User '{user.full_name}' has been deleted.")
            print("May we keep growing in grace daily.")
            print("--------------------------------------------------")
        except Exception as e:
            session.rollback()
            print("Error deleting user:", e)
    else:
        print("User not found.")


def show_all_users():
    users = session.query(User).all()
    if not users:
        print("\n--------------------------------------------------")
        print("No users found.")
        print("You can start by creating your first user.")
        print("--------------------------------------------------")
        return

    print("\n--------------------------------------------------")
    print(" Registered Users:\n")

    for u in users:
        print("--------------------------------------------------")
        print(f"ID       : {u.id}")
        print(f"Name     : {u.full_name}")
        print(f"Email    : {u.email}")
        print(f"Age      : {u.age if u.age else 'N/A'}")
        print(f"Gender   : {u.gender if u.gender else 'N/A'}")
    print("--------------------------------------------------")
    print("Each user is precious and known by name.")
    print("--------------------------------------------------")


def view_user_devotion_sessions():
    email = input("Enter the user's email: ").strip()
    user = session.query(User).filter_by(email=email).first()

    if not user:
        print("\n--------------------------------------------------")
        print("User not found. Make sure the email is correct.")
        print("--------------------------------------------------")
        return

    if not user.devotion_sessions:
        print("\n--------------------------------------------------")
        print(f"No devotion sessions found for {user.full_name}.")
        print("Encourage them to spend time in the Word today.")
        print("--------------------------------------------------")
        return

    print("\n--------------------------------------------------")
    print(f" Devotion Sessions for {user.full_name}:\n")

    for s in user.devotion_sessions:
        print("--------------------------------------------------")
        print(f"Session ID   : {s.id}")
        print(f"Date         : {s.date}")
        print(f"Scripture    : {s.scripture_read}")
        print(f"Reflection   : {s.reflection}")
    print("--------------------------------------------------")
print("He rewards those who earnestly seek Him. – Hebrews 11:6")
print("--------------------------------------------------")

def find_user_by_email():
    email = input("Enter email to search: ").strip()
    user = session.query(User).filter_by(email=email).first()

    if not user:
        print("\n--------------------------------------------------")
        print("No user found with that email.")
        print("Make sure it's typed correctly.")
        print("--------------------------------------------------")
        return

    print("\n--------------------------------------------------")
    print(" User Details:\n")
    print("--------------------------------------------------")
    print(f"Name     : {user.full_name}")
    print(f"Email    : {user.email}")
    print(f"Age      : {user.age if user.age else 'N/A'}")
    print(f"Gender   : {user.gender if user.gender else 'N/A'}")
    print("--------------------------------------------------")
    print("You are fearfully and wonderfully made. – Psalm 139:14")
    print("--------------------------------------------------")


# ----------------- CATEGORY MENU -----------------
def category_menu():
    while True:
        print("\n----- Category Menu ------")
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
    print("\n--------------------------------------------------")
    print(f"Category '{name}' created successfully.")
    print("Let every word lead you closer to Him.")
    print("--------------------------------------------------")


def delete_category():
    name = input("Enter category name to delete: ").strip()
    category = session.query(Category).filter_by(name=name).first()
    if category:
        session.delete(category)
        session.commit()
        print("\n--------------------------------------------------")
        print(f"Category '{name}' has been deleted.")
        print("Keep organizing your time with the Lord intentionally.")
        print("--------------------------------------------------")
    else:
        print("Category not found.")

def show_all_categories():
    categories = session.query(Category).all()
    if not categories:
        print("\n--------------------------------------------------")
        print("No categories available.")
        print("Consider creating categories like Prayer, Study, Worship.")
        print("--------------------------------------------------")
        return

    print("\n--------------------------------------------------")
    print(" Available Devotion Categories:\n")

    for c in categories:
        print("--------------------------------------------------")
        print(f"ID    : {c.id}")
        print(f"Name  : {c.name}")
    print("--------------------------------------------------")
    print("Let everything be done for the glory of God. – 1 Cor 10:31")
    print("--------------------------------------------------")


# ----------------- DEVOTION SESSION MENU -----------------
def devotion_session_menu():
    while True:
        print("\n------ Devotion Session Menu ------")
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
    print("\n--------------------------------------------------")
    print("Devotion session recorded successfully.")
    print("Your quiet time matters. Keep going.")
    print("--------------------------------------------------")


def delete_devotion_session():
    session_id = input("Enter Devotion Session ID to delete: ").strip()
    session_obj = session.query(DevotionSession).filter_by(id=session_id).first()
    if session_obj:
        session.delete(session_obj)
        session.commit()
        print("\n--------------------------------------------------")
        print("Devotion session deleted successfully.")
        print("Thank you for being intentional with your walk.")
        print("--------------------------------------------------")
    else:
        print("Devotion session not found.")


def show_all_devotion_sessions():
    sessions_list = session.query(DevotionSession).all()
    if not sessions_list:
        print("\n--------------------------------------------------")
        print("No devotion sessions found.")
        print("Your journey with God is worth recording. Start now.")
        print("--------------------------------------------------")
        return

    print("\n--------------------------------------------------")
    print(" Devotion Sessions Log:\n")

    for s in sessions_list:
        print("--------------------------------------------------")
        print(f"Session ID   : {s.id}")
        print(f"User         : {s.user.full_name}")
        print(f"Category     : {s.category.name}")
        print(f"Date         : {s.date.strftime('%Y-%m-%d')}")
        print(f"Scripture    : {s.scripture_read}")
        print(f"Reflection   : {s.reflection}")
    print("--------------------------------------------------")
    print("Your faithfulness is seen by the One who matters most.")
    print("--------------------------------------------------")



# ----------------- FAVORITE VERSE MENU -----------------
def favorite_verse_menu():
    while True:
        print("\n------- Favorite Verse Menu --------")
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
    print("\n--------------------------------------------------")
    print("Favorite verse added successfully.")
    print("May His Word continue to dwell richly in you.")
    print("--------------------------------------------------")


def remove_favorite_verse():
    verse_id = input("Enter Favorite Verse ID to delete: ").strip()
    fv = session.query(FavoriteVerse).filter_by(id=verse_id).first()
    if fv:
        session.delete(fv)
        session.commit()
        print("\n--------------------------------------------------")
        print("Favorite verse deleted successfully.")
        print("Continue treasuring His word in your heart.")
        print("--------------------------------------------------")
    else:
        print("Favorite verse not found.")

def show_all_favorite_verses():
    verses = session.query(FavoriteVerse).all()
    if not verses:
        print("\n--------------------------------------------------")
        print("No favorite verses found.")
        print("Start treasuring God’s Word in your heart.")
        print("--------------------------------------------------")
        return

    print("\n--------------------------------------------------")
    print(" Favorite Bible Verses:\n")

    for v in verses:
        print("--------------------------------------------------")
        print(f"ID      : {v.id}")
        print(f"User    : {v.user.full_name}")
        print(f"Verse   : {v.verse_text}")
    print("--------------------------------------------------")
    print("His Word is a lamp to your feet and a light to your path. – Psalm 119:105")
    print("--------------------------------------------------")


if __name__ == "__main__":
    main_menu()