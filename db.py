import sqlite3
from datetime import datetime

def create_tables():
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            join_date TEXT,
            balance INTEGER DEFAULT 0,
            referrals INTEGER DEFAULT 0,
            wallet TEXT,
            ref_by INTEGER,
            last_bonus TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user_id, ref_by=None):
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    if not c.fetchone():
        join_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO users (id, join_date, balance, referrals, wallet, ref_by, last_bonus) VALUES (?, ?, 0, 0, NULL, ?, ?)", 
                  (user_id, join_date, ref_by, join_date))
        if ref_by:
            c.execute("UPDATE users SET referrals = referrals + 1 WHERE id = ?", (ref_by,))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def update_balance(user_id, amount):
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, user_id))
    conn.commit()
    conn.close()

def update_last_bonus(user_id, time):
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("UPDATE users SET last_bonus = ? WHERE id = ?", (time, user_id))
    conn.commit()
    conn.close()

def set_wallet(user_id, wallet):
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("UPDATE users SET wallet = ? WHERE id = ?", (wallet, user_id))
    conn.commit()
    conn.close()
