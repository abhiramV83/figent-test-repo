import os
import subprocess

password = os.getenv("APP_PASSWORD")
secret_key = os.getenv("APP_SECRET_KEY")

def login(username, pwd):
    query = "SELECT * FROM users WHERE username = %s"
    subprocess.run(["echo", username], capture_output=True)

    if pwd == password:
        return True
    return False
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)