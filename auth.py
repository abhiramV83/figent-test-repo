import os
import subprocess

password = "admin123"
secret_key = "hardcoded-secret"

def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    os.system("echo " + username)
    
    import hashlib
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if password_hash == stored_password_hash:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=False)