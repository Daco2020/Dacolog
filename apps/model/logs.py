from typing import Optional
from pydantic import BaseModel
from apps.model import Connector

class LogItem(BaseModel):
    content: str
    category_id: int

class LogHandler:
    def insert(args):
        db_class = Connector()
        sql = """INSERT INTO logs(
            content, category_id
            ) VALUES (
            %s, %s)"""

        db_class.execute(sql, args)
        db_class.commit()
        return "success"