import os
import subprocess

stored_password = os.getenv("APP_PASSWORD")
secret_key = os.getenv("APP_SECRET_KEY")

def login(username, password):
    query = "SELECT * FROM users WHERE username = ?"
    # Execute with a DB cursor using parameters, e.g., cursor.execute(query, (username,))
    print(f"Login attempt for user: {username}")
    
    if password == stored_password:
        return True
    return False
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)