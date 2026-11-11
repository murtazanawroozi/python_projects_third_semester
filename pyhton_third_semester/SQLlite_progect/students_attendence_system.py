import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students (id)
    )
"""
)
conn.commit()


def add_student(name):
    cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
    conn.commit()


def record_attendance(student_id, date, status):
    cursor.execute(
        "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
        (student_id, date, status),
    )
    conn.commit()


def get_report():
    cursor.execute(
        """
        SELECT students.name, attendance.date, attendance.status 
        FROM attendance 
        JOIN students ON attendance.student_id = students.id
    """
    )
    return cursor.fetchall()