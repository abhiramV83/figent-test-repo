import os
import subprocess

STORED_PASSWORD = os.getenv("APP_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")

def login(username, password):
    query = "SELECT * FROM users WHERE username = ?"
    query_params = (username,)
    # Use a database cursor to execute the parameterized query, e.g., cursor.execute(query, query_params)
    print(username)

    if password == STORED_PASSWORD:
        return True
    return False

def run_command(cmd_args):
    subprocess.run(cmd_args, check=True)