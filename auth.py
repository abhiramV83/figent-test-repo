import os
import subprocess

# password removed for security
# secret_key removed for security

def login(username, pwd):
    # query = "SELECT * FROM users WHERE username = ?"  # Use parameterized queries
    subprocess.run(["echo", username], check=True)

    if pwd == os.getenv('ADMIN_PASSWORD'):
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)