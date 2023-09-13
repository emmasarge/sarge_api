import os
from dotenv import dotenv_values
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()
root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
env_path = os.path.join(root_folder, ".env")

config = dotenv_values(env_path)
ADMIN_USERNAME = os.environ.get("ADMIN_UN")
ADMIN_PW = os.environ.get("ADMIN_PW")

def authenticate(credentials: HTTPBasicCredentials = Security(security)):
    if credentials.username != ADMIN_USERNAME or credentials.password != ADMIN_PW:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True
