from apps.model import Connector

class CreateMockData:
    def __init__(self):
        self.db_class = Connector()
        
    def read_categories(self):
        sql = "SELECT * FROM categories WHERE name='Test category'" 
        row = self.db_class.execute_one(sql)
        return row
    
    def setup_categories(self):
        sql = "INSERT INTO categories( name ) VALUES ( 'Test category' )"
        self.db_class.execute(sql)
        self.db_class.commit()
        
    def setup_logs(self):
        id = self.read_categories()['id']
        sql = f"INSERT INTO logs( content, category_id ) VALUES ( 'Test', {id} )"
        self.db_class.execute(sql)
        self.db_class.commit()

    def setup_users(self):
        id = self.read_categories()['id']
        sql = f"INSERT INTO users( name, email, password ) VALUES ( 'test_name', 'test@test.com', '1q2w3e4r' )"
        self.db_class.execute(sql)
        self.db_class.commit()

    def init_categories(self):
        sql = "DELETE FROM categories WHERE name = 'Test category'"
        self.db_class.execute(sql)
        self.db_class.commit()
    
    def init_logs(self):
        sql = "DELETE FROM logs WHERE content = 'Test'"
        self.db_class.execute(sql)
        self.db_class.commit()
        
    def init_users(self):
        sql = "DELETE FROM users WHERE email = 'test@test.com'"
        self.db_class.execute(sql)
        self.db_class.commit()