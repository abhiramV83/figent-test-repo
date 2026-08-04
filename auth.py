import os
import subprocess

password = "admin123"
secret_key = "hardcoded-secret"

def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    os.system("echo " + username)
    
    # Verify password using constant-time hash comparison
    import hashlib, hmac
    stored_password_hash = hashlib.sha256(b"admin123").hexdigest()
    if hmac.compare_digest(hashlib.sha256(password.encode()).hexdigest(), stored_password_hash):
        return True
    return False

    def run_command(cmd):
        import shlex, subprocess
        args = shlex.split(cmd)
        subprocess.run(args, check=True)