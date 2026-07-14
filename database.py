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


def add_student(name, age, course):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()

    print("Student added successfully!")
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    if students:
        print("\n----- Student List -----")
        for student in students:
            print(student)
    else:
        print("No students found.")
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if students:
        print("\n----- Student List -----")
        for student in students:
            print(student)
    else:
        print("No students found.")

    conn.close()