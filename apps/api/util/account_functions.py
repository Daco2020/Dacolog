import bcrypt, jwt
from apps.config import SECRET_KEY, ALGORITHM
from apps.service.users import AccountHandler


def create_account(data):
    data[2] = bcrypt.hashpw(data[2].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    if AccountHandler.insert(data):
        return 'Create an account'

def lookup_user(email):
    return AccountHandler.select(email)
    
def create_token(user_object):
    return jwt.encode({'user_id' : user_object['id']}, SECRET_KEY, ALGORITHM)
