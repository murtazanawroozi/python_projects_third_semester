import sqlite3

with sqlite3.connect("system.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        email TEXT UNIQUE
    )
    """)
    cursor.execute("DELETE FROM users")
    conn.commit()

def register_user(username, email):
    try:
        with sqlite3.connect("system.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
            conn.commit()
            print(f"User '{username}' registered successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Registration failed for '{username}'. Error detail: {e}")

print("--- Initial Registrations ---")
register_user("mechanic_jack", "jack@example.com")
register_user("coding_ninja", "ninja@example.com")

print("\n--- Testing Unique Constraint Violations ---")
register_user("mechanic_jack", "new_jack@example.com")
register_user("shadow_user", "ninja@example.com")