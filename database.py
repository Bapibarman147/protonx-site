import sqlite3
from datetime import datetime

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        join_date TEXT,
        balance INTEGER DEFAULT 0,
        referred_by INTEGER,
        referrals INTEGER DEFAULT 0
    )
''')
conn.commit()

def add_user(user_id, username, referred_by=None):
    join_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    if c.fetchone() is None:
        c.execute('''
            INSERT INTO users (user_id, username, join_date, referred_by)
            VALUES (?, ?, ?, ?)
        ''', (user_id, username, join_date, referred_by))
        if referred_by:
            c.execute('UPDATE users SET referrals = referrals + 1 WHERE user_id = ?', (referred_by,))
        conn.commit()

def get_user(user_id):
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return c.fetchone()

def get_balance(user_id):
    c.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    return result[0] if result else 0
