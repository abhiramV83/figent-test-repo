import os
import subprocess

password = "admin123"
secret_key = "hardcoded-secret"

def login(username, password):
    import hashlib
    # Retrieve stored password hash securely (implementation omitted)
    stored_hash = get_user_password_hash(username)
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return password_hash == stored_hash

def run_command(cmd):
    # Execute command without using a shell to avoid injection
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode