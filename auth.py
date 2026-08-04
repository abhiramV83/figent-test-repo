import os
import subprocess

EXPECTED_PASSWORD = os.getenv('APP_PASSWORD')
SECRET_KEY = os.getenv('APP_SECRET_KEY')

def login(username, password):
    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = %s"
    # Execute query safely with a DB cursor (implementation omitted)
    if password == EXPECTED_PASSWORD:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)