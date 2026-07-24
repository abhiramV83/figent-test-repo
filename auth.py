import os
import subprocess

password = os.getenv("APP_PASSWORD")
secret_key = os.getenv("APP_SECRET_KEY")

def login(username, pwd):
# Parameterized query should be used with a DB library; omitted here
subprocess.run(["echo", username], check=True)

if pwd == password:
    return True
return False

def run_command(cmd):
subprocess.run(cmd, check=True)