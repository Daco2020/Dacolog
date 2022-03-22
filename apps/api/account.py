import json, bcrypt, jwt
from fastapi import Request, APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from apps.service.users import AccountLoginItem, AccountSignupItem
from apps.api.util.account_functions import *
from apps.api.util.validations import *



router = APIRouter(
    prefix="/account"
)


@router.post("")
async def signup(request: Request, account_signup_item: AccountSignupItem):
    try:
        name = account_signup_item.name
        email = account_signup_item.email
        password = account_signup_item.password
        check_email_already_exists(email)
        check_email_regex(email)
        check_password_regex(password)
        result = create_account([name, email, password])
        
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={'message' : result})
    
    except HTTPException as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message' : err.detail})


@router.post("/login")
async def login(request: Request, account_login_item: AccountLoginItem):
    try:
        email = account_login_item.email
        password = account_login_item.password
        user_object = lookup_user(email)
        check_account_match(password, user_object)
        token = create_token(user_object)
        
        return JSONResponse(status_code=status.HTTP_200_OK, content={'message' : 'success', 'access_token' : token})
    
    except HTTPException as err:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={'message' : err.detail})