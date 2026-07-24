import os
import subprocess

password = "admin123"
secret_key = "hardcoded-secret"

def login(username, password):
    import sqlite3
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    if row and row[0] == password:
        return True
    return False

def run_command(cmd):
    subprocess.run(cmd, shell=False, check=True)