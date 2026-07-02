import os
import subprocess

password = "admin123"
secret_key = "hardcoded-secret"

def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    os.system("echo " + username)
    
    if password == "admin123":
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)