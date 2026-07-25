import os
import subprocess

# password removed - use secure storage
# secret_key removed - use environment variable

def login(username, password):
    query = ("SELECT * FROM users WHERE username = ?", (username,))  # parameterized query
    subprocess.run(["echo", username], check=True)
    
    # TODO: implement secure password verification
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)