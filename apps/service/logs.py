from pydantic import BaseModel
from apps.model import Connector

class LogItem(BaseModel):
    content: str
    category_id: int

class LogHandler:
    # 유저인증인가 구현 후 user_id 조건 추가예정
    def insert(args):
        db_class = Connector()
        sql = """INSERT INTO logs(
            content, category_id
            ) VALUES (
            %s, %s)"""

        db_class.execute(sql, args)
        db_class.commit()
        return True
    
    def select_all():
        db_class = Connector()
        sql = "SELECT * FROM logs ORDER BY created_at DESC LIMIT 100" 
        rows = db_class.execute_all(sql)
        return rows
    
    def delete(args):
        db_class = Connector()
        sql = "DELETE FROM logs WHERE content = %s"
            
        db_class.execute(sql, args)
        db_class.commit()
        return True