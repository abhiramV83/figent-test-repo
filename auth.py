import os
import subprocess

def login(username, password):
import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
# Process the query result as needed
# Removed insecure os.system call
# Password should be verified against stored hash; placeholder verification function used
if verify_password(username, password):
    return True
return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)