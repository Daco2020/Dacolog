import json, bcrypt, jwt
from fastapi import Request, APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from apps.service.users import AccountSignupItem, AccountHandler
from apps.api.util.validation import check_email_exists, check_email_regex, check_password_regex


router = APIRouter(
    prefix="/account"
)

def create_account(data):
    data[2] = bcrypt.hashpw(data[2].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    if not AccountHandler.insert(data):
        raise HTTPException(status_code=400, detail="Could not create account")
    

@router.post("/")
async def signup(request: Request, account_signup_item: AccountSignupItem):
    try:
        name = account_signup_item.name
        email = account_signup_item.email
        password = account_signup_item.password
        
        check_email_regex(email)
        check_email_exists(email)
        check_password_regex(password) 
        
        data = [name, email, password]

        create_account(data)
        
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={'message' : 'success'})
    
    except HTTPException as error:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message' : error.detail})