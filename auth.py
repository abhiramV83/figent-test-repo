import os
import subprocess

password = "admin123"
secret_key = "hardcoded-secret"
USERS = {"admin": "admin123"}


def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    os.system("echo " + username)
    
    if username in USERS and password == USERS[username]:
        return True
    return False


def run_command(cmd):
    subprocess.call(cmd, shell=False)