import os
import subprocess

# Retrieve credentials from environment variables
PASSWORD = os.getenv("APP_PASSWORD")
SECRET_KEY = os.getenv("APP_SECRET_KEY")

def login(username, pwd):
    # Example of safe query usage with a DB library (placeholder)
    # query = "SELECT * FROM users WHERE username = %s"
    # cursor.execute(query, (username,))
    subprocess.run(["echo", username], check=False)

    if pwd == PASSWORD:
        return True
    return False

def run_command(cmd):
    subprocess.run(cmd, check=False)