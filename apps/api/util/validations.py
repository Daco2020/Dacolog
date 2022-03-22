import re, bcrypt
from fastapi import HTTPException
from apps.service.users import AccountHandler
from apps.api.util.account_functions import lookup_user

def check_email_regex(email):
    if not re.match("[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email):
        raise HTTPException(status_code=400, detail="Email is invalid")

def check_password_regex(password):
    if not re.match("(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}", password):
        raise HTTPException(status_code=400, detail="Password is invalid")
    
def check_email_already_exists(email):
    if lookup_user(email):
        raise HTTPException(status_code=400, detail="Email already exists")
    
def check_account_match(password, user_object):
    if not user_object or not bcrypt.checkpw(password.encode('utf-8'), user_object['password'].encode('utf-8')):
        raise HTTPException(status_code=401, detail="Account does not match")
