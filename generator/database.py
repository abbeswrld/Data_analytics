import psycopg2
from config import config

class Database:
    def __init__(self):
        self._conn = None
        self._cursor = None
    
    def connect(self):
        self._conn = psycopg2.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            database=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD
        )
        self._cursor = self._conn.cursor()
        return self._conn, self._cursor
    
    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._conn:
            self._conn.close()
            
    @property
    def cursor(self):
        return self._cursor
    
    @property
    def connection(self):
        return self._conn
    