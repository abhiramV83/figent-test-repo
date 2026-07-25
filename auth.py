import os
import subprocess

def login(username, password):
    # TODO: implement secure password verification
    # Use parameterized queries with a database cursor (implementation omitted)
    print(f"Login attempt for user: {username}")
    
    if password == "admin123":
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)