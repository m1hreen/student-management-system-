import sqlite3

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database created successfully!")
    from database import create_database

def main():
    print("===================================")
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("===================================")

    create_database()

    print("Welcome to the Student Management System!")

if __name__ == "__main__":
    main()