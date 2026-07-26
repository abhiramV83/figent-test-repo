import os
import subprocess

password = os.getenv('APP_PASSWORD')
secret_key = os.getenv('SECRET_KEY')

def login(username, pwd):
    # Parameterized query placeholder (actual execution should use DB API with parameters)
    query = "SELECT * FROM users WHERE username = %s"
    # Removed insecure os.system call
    if pwd == password:
        return True
    return False

def run_command(cmd):
    subprocess.call(cmd, shell=True)