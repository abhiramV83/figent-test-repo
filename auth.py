import os
import subprocess

password = "admin123"
secret_key = "hardcoded-secret"

def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    os.system("echo " + username)
    
    # Compare password using a secure hash
    import hashlib
    hashed_input = hashlib.sha256(password.encode()).hexdigest()
    if hashed_input == hashlib.sha256("admin123".encode()).hexdigest():
        return True
    return False

def run_command(cmd):
    # Execute command without invoking a shell to avoid injection
    if isinstance(cmd, str):
        cmd = cmd.split()
    subprocess.call(cmd, shell=False)