import os
import subprocess

stored_password = os.getenv("APP_PASSWORD")
secret_key = os.getenv("SECRET_KEY")

def login(username, pwd):
    query = ("SELECT * FROM users WHERE username = ?", (username,))
    subprocess.run(["echo", username], check=True)

    if pwd == stored_password:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)