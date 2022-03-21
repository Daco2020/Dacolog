import re
from fastapi import HTTPException
from apps.service.users import AccountHandler

def check_email_regex(email):
    if not re.match("[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email):
        raise HTTPException(status_code=400, detail="Email is invalid")

def check_password_regex(password):
    if not re.match("(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}", password):
        raise HTTPException(status_code=400, detail="Password is invalid")
    
def check_email_exists(email):
    if AccountHandler.select(email):
        raise HTTPException(status_code=400, detail="Email already exists")