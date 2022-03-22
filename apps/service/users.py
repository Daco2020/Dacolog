from pydantic import BaseModel
from apps.model import Connector

class AccountSignupItem(BaseModel):
    name : str
    email : str
    password : str

class AccountLoginItem(BaseModel):
    email : str
    password : str

class AccountHandler:
    def insert(args):
        db_class = Connector()
        sql = """INSERT INTO users(
            name, email, password
            ) VALUES (
            %s, %s, %s)"""
            
        db_class.execute(sql, args)
        db_class.commit()
        return True
    
    def select(args):
        db_class = Connector()
        sql = "SELECT * FROM users WHERE email=%s" 
        row = db_class.execute_one(sql, args)
        return row