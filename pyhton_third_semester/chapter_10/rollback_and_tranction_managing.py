import sqlite3

with sqlite3.connect("banking.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INTEGER PRIMARY KEY,
        owner TEXT NOT NULL,
        balance REAL NOT NULL
    )
    """)
    conn.commit()

def reset_accounts():
    with sqlite3.connect("banking.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM accounts")
        cursor.execute("INSERT INTO accounts VALUES (1, 'Ali', 500.0)")
        cursor.execute("INSERT INTO accounts VALUES (2, 'Sara', 200.0)")
        conn.commit()

def transfer_money(from_id, to_id, amount):
    conn = sqlite3.connect("banking.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_id,))
        sender_balance = cursor.fetchone()[0]
        
        if sender_balance < amount:
            raise ValueError("Insufficient funds")
            
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_id))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_id))
        
        conn.commit()
        print("Transfer completed successfully.")
    except (sqlite3.Error, ValueError) as e:
        conn.rollback()
        print("Transaction failed. Changes rolled back. Reason:", e)
    finally:
        conn.close()

reset_accounts()
print("--- Attempting Invalid Transfer (Overdraft) ---")
transfer_money(1, 2, 600.0)

print("\n--- Attempting Valid Transfer ---")
transfer_money(1, 2, 150.0)