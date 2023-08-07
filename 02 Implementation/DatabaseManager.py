import mysql.connector


class databaseManager:
    def __init__(self, Core):
        core = Core
        # db = self.connect()
        # self.myCursor = db.cursor()
        # self.Querie()

    def connect(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mclarenf1@"
        )
        return db

    def CheckLoginInfo(self, data):
        db = self.connect()
        myCursor = db.cursor()
        myCursor.execute(f"SELECT Password FROM testing.logins WHERE ID = {data['ID']};")
        password = myCursor.fetchone()
        if password[0] == data["Password"]:
            return True
        return False
