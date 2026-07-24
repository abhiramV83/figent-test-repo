import os
import subprocess

import sqlite3
DB_PATH = os.getenv("DB_PATH", "app.db")
SECRET_KEY = os.getenv("SECRET_KEY")

def login(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    # Process query result as needed
    subprocess.run(["echo", username], check=False)
    conn.close()
    expected_password = os.getenv("ADMIN_PASSWORD")
    return password == expected_password

def run_command(cmd):
    subprocess.call(cmd, shell=True)