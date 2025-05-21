import sqlite3

def init_db():
    conn = sqlite3.connect('signatures.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    original TEXT,
                    test TEXT,
                    similarity REAL
                 )''')
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    username TEXT UNIQUE,
                    password TEXT NOT NULL
                 )''')
    conn.commit()
    conn.close()

def save_result(original, test, similarity):
    conn = sqlite3.connect('signatures.db')
    c = conn.cursor()
    c.execute("INSERT INTO results (original, test, similarity) VALUES (?, ?, ?)", (original, test, similarity))
    conn.commit()
    conn.close()

def get_all_results():
    conn = sqlite3.connect('signatures.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM results")
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def save_user(full_name, username, password):
    conn = sqlite3.connect('signatures.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)", (full_name, username, password))
    conn.commit()
    conn.close()

def validate_user(username, password):
    conn = sqlite3.connect('signatures.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None
