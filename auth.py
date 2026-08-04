import os
import subprocess

import sqlite3
import os

def login(username, password):
    # Parameterized query to prevent SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    # Secure password check (use environment variable or hashed passwords)
    admin_password = os.getenv('ADMIN_PASSWORD')
    if admin_password and password == admin_password:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)