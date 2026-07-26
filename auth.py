import os
import subprocess

password = os.getenv("ADMIN_PASSWORD")
secret_key = os.getenv("SECRET_KEY")

def login(username, pwd):
    query = "SELECT * FROM users WHERE username = %s"
    params = (username,)
    subprocess.run(["echo", username], check=True)

    if pwd == password:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)