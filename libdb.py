import mysql.connector
import os

class Database:

    def __init__(self):

        self.dbobj = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv(
        "DB_NAME",
        "library_management_system_oops"
    )
)

        self.dbcursor = self.dbobj.cursor()
        
        


database = Database()


