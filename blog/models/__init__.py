import pymysql
from app.config import DATABASE

class Connector():
    def __init__(self):
        self.db = None
        self.cursor = None
        
    def connect(self):
        self.db = pymysql.connect(**DATABASE)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        print("DB가 연결되었습니다.")

    # 단일 인서트
    def execute(self, query, args={}):
        self.cursor.execute(query, args) 

    # 벌크 인서트(추가)
    def execute_many(self, query, args={}):
        self.cursor.executemany(query, args)         

    # 한번에 한 row
    def execute_one(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    # 모든 row
    def execute_all(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
        
connector = Connector()