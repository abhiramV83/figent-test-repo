import os
import subprocess

# Removed hardcoded credentials; use environment variables

def login(username, pwd):
    # Use parameterized query to avoid SQL injection
    query = "SELECT * FROM users WHERE username = %s"
    # Password verification against environment variable
    expected_pwd = os.getenv("APP_PASSWORD")
    if expected_pwd is None:
        return False
    if pwd == expected_pwd:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)