# QuietTime Devotion Tracker

A command-line application to help users track their daily devotion habits, favorite Bible verses, and organize their reflections by category.

## Description

**QuietTime Devotion Tracker** is a Python-based CLI app that allows users to:
- Create and manage devotion sessions
- Organize their reflections by category
- Store and retrieve their favorite Bible verses
- Track personal spiritual growth over time

It uses SQLAlchemy ORM with a normalized SQLite database and features a clean command-line interface.

---
## Project Owner

**Grace Zawadi**

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Chenzie2/QuietTime-Devotion-Tracker.git
cd QuietTime-Devotion-Tracker
```

### 2. Create & Activate Virtual Environment
```bash
pipenv install
pipenv shell
```

### 3. Run Database Migrations
```bash
alembic upgrade head
```

### 4. Launch the Application
```bash
python lib/cli.py
```
---
###  Features

- **User Management**
  - Create, view, find, and delete users
  - Search users by email
  - View a user's devotion sessions

- **Devotion Sessions**
  - Log devotion sessions with scripture and reflections
  - Associate sessions with categories
  - View and delete existing sessions

- **Favorite Verses**
  - Add favorite Bible verses per user
  - View all favorite verses
  - Remove specific verses

- **Category Management**
  - Create and delete categories for devotion sessions
  - View all available categories

- **Command-Line Interface**
  - Menu-driven interface with clear navigation
  - Input validation and helpful error messages

- **Persistent Storage**
  - Data stored in SQLite database
  - Alembic used for versioned schema migrations


### Technologies Used

- **Python 3** — Core programming language
- **SQLite** — Lightweight database for data persistence
- **SQLAlchemy** — ORM to interact with the database using Python
- **Alembic** — Handles database migrations
- **Pipenv** — Manages dependencies and virtual environments
- **CLI Interface** — Built using standard `input()` and `print()` functions
---

### Folder Structure
```bash
QuietTime-Devotion-Tracker/
.
├── alembic
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 8cc903378bdb_initial_schema.py
│       └── a800969b8ae9_add_title_column_to_devotion_sessions.py
├── alembic.ini
├── lib
│   ├── cli.py
│   ├── debug.py
│   ├── models
│   │   ├── category.py
│   │   ├── devotion_session.py
│   │   ├── favorite_verse.py
│   │   ├── __init__.py
│   │   └── user.py
│   └── seed.py
├── Pipfile
├── Pipfile.lock
├── quiettime_devotion_tracker.db
└── README.md
```
---

## Support/Contact
For questions or feedback, please reach out via GitHub: @Chenzie2

### License

This project is licensed under the [MIT License] 
You are free to use, modify, and distribute this project with proper attribution.

&copy; 2025 Grace Zawadi
