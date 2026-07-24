import os
import subprocess

import hashlib
import sqlite3

password = os.getenv("DB_PASSWORD")
secret_key = os.getenv("SECRET_KEY")

def login(username, password):
    # Parameterized query to avoid SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    # Safely echo username without invoking a shell
    subprocess.run(["echo", username], check=False)
    row = cursor.fetchone()
    if row and hashlib.sha256(password.encode()).hexdigest() == row[2]:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)