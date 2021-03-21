import sqlite3
from sqlite3 import Error

class PassnerDatabase():
    def __init__(self, path):
        self.path = path
        self.conn = None
        self.cursor = None
        self.mainTable = """ 
            CREATE TABLE IF NOT EXISTS main (
                id integer PRIMARY KEY,
                user text NOT NULL,
                password text NOT NULL,
                info text
            ); """
        self.keyMasterTable = " CREATE TABLE IF NOT EXISTS keyMaster ( key text NOT NULL, ba64 NOT NULL); "

    def existTables(self):
        try:
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            r = self.cursor.fetchall()
            if len(r) != 2: return False
            return True
        except Error as e: print(e)

    def getAccounts(self):
        try:
            self.cursor.execute("SELECT * FROM main")
            r = self.cursor.fetchall()
            if len(r) == 0: return False
            print(r)
            return r
        except Error as e: print(e)

    def getKeyMaster(self):
        try:
            self.cursor.execute("SELECT key FROM keyMaster")
            rows = self.cursor.fetchall()
            if len(rows) == 0: return False
            key = rows[0][0]
            return [key[:87], key[87:]]
        except Error as e: print(e)
    
    def deleteAccount(self, id):
        try:
            self.cursor.execute(f'DELETE FROM main WHERE id = {id};')
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False
        
    def addAccount(self, data):
        try: 
            self.cursor.execute(f'INSERT INTO main (user, password, info) VALUES (?, ?, ?)', data)
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False
        
    def addKeyMaster(self, key):
        try: 
            self.cursor.execute(f'INSERT INTO keyMaster (key) VALUES (?)', (key,))
            self.conn.commit()
        except Error as e:
            print(e)

    def createTables(self):
        self.cursor.execute(self.mainTable)
        self.cursor.execute(self.keyMasterTable)

    def createConnection(self):
        try:
            self.conn = sqlite3.connect(self.path)
            self.cursor = self.conn.cursor()
            return True
        except Error as e:
            print(e)
            return False

    def closeConnection(self): 
        if self.conn: self.conn.close()