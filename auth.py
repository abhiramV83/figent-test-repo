import os
import subprocess, hashlib

hashed_password = hashlib.sha256(b"admin123").hexdigest()
secret_key = "hardcoded-secret"

def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    os.system("echo " + username)
    
    if hashlib.sha256(password.encode()).hexdigest() == hashed_password:
        return True
    return False

def run_command(cmd):
    subprocess.run(cmd, shell=False, check=False)