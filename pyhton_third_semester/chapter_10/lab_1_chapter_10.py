import sqlite3

def init_database():
    with sqlite3.connect("academy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            department TEXT,
            semester INTEGER
        )
        """)
        conn.commit()

def add_student(name, email, department, semester):
    try:
        with sqlite3.connect("academy.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO students (name, email, department, semester)
            VALUES (?, ?, ?, ?)
            """, (name, email, department, semester))
            conn.commit()
            print("Student added successfully.")
    except sqlite3.IntegrityError as e:
        print("Constraint error (e.g. Email already exists):", e)
    except sqlite3.Error as e:
        print("Database error:", e)

def add_multiple_students(students_list):
    try:
        with sqlite3.connect("academy.db") as conn:
            cursor = conn.cursor()
            cursor.execute_many("""
            INSERT INTO students (name, email, department, semester)
            VALUES (?, ?, ?, ?)
            """, students_list)
            conn.commit()
            print(f"Batch insert successful. Rows affected: {cursor.rowcount}")
    except sqlite3.Error as e:
        print("Batch insertion failed:", e)

def view_all_students():
    with sqlite3.connect("academy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def search_students_by_semester(semester):
    with sqlite3.connect("academy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id, name, email 
        FROM students 
        WHERE semester = ?
        """, (semester,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def update_student_academic(student_id, new_dept, new_semester):
    with sqlite3.connect("academy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE students
        SET department = ?, semester = ?
        WHERE id = ?
        """, (new_dept, new_semester, student_id))
        conn.commit()
        print(f"Update done. Rows affected: {cursor.rowcount}")

def delete_student(student_id):
    with sqlite3.connect("academy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM students
        WHERE id = ?
        """, (student_id,))
        conn.commit()
        print(f"Deletion done. Rows affected: {cursor.rowcount}")

init_database()

print("--- Adding Individual Student ---")
add_student("Ahmad", "ahmad@example.com", "Software Engineering", 3)

print("\n--- Adding Multiple Students ---")
batch = [
    ("Ali", "ali@example.com", "SE", 3),
    ("Sara", "sara@example.com", "IT", 2),
    ("Omid", "omid@example.com", "IS", 4)
]
add_multiple_students(batch)

print("\n--- Viewing All Records ---")
view_all_students()

print("\n--- Searching by Semester (Semester 3) ---")
search_students_by_semester(3)

print("\n--- Updating Ahmed's Record (ID: 1) ---")
update_student_academic(1, "Information Technology", 4)

print("\n--- Deleting Record (ID: 4) ---")
delete_student(4)

print("\n--- Final Database State ---")
view_all_students()