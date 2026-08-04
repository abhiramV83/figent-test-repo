import os
import subprocess

password = os.getenv("APP_PASSWORD")
secret_key = os.getenv("APP_SECRET_KEY")

def login(username, pwd):
    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    # Log login attempt without exposing sensitive data
    print(f"Login attempt for user: {username}")

    if pwd == password:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)