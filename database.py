import sqlite3

def create_tables():
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            balance INTEGER DEFAULT 0,
            join_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user_id, name):
    import datetime
    join_date = datetime.datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (id, name, join_date) VALUES (?, ?, ?)", (user_id, name, join_date))
    conn.commit()
    conn.close()

def get_user_info(user_id):
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user
