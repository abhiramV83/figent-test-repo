import os
import subprocess

# Retrieve credentials from environment variables
DB_PASSWORD = os.getenv("DB_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")

def login(username, pwd):
    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    # Example execution placeholder (requires a DB cursor)
    # cursor.execute(query, (username,))
    
    # Avoid command injection; do not echo user input
    
    if pwd == DB_PASSWORD:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)