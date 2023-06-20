import json
from typing import Tuple, List


class database:

    def __init__(self):
        self.unformattedData = None
        self.formattedData = None
        pass

    def loadDatabase(self, filepath: str) -> None:
        """
        Reads and loads the database information into the initialised class
        :param filepath:
        :return:
        """

        with open(filepath) as json_file:
            data = json.loads(json_file.read())
        json_file.close()

        self.formattedData = data

    def outData(self) -> str:
        """
        Returns the formatted data
        :return:
        """
        return self.formattedData

    def checkUsernameAndPassword(self, username: str, password: str) -> bool:
        """
        Checks if the username or password for the chosen database exists
        :param username:
        :param password:
        :return: True/False
        """
        data = self.formattedData
        result = False
        try:
            loginInfo = data["LoginInfo"]
            for dicts in loginInfo:
                if dicts["username"] == username:
                    if dicts["password"] == password:
                        result = True
                        break
        except Exception as e:
            raise Exception(e)

        return result

    def getUserID(self,username: str) -> str:
        """
        Returns the ID based on the username
        :param username:
        :return:
        """
        data = self.formattedData
        id = ""
        try:
            loginInfo =data["LoginInfo"]
            for dicts in loginInfo:
                if dicts["username"] == username:
                    id = dicts["ID"]
                    break
        except Exception as e:
            raise Exception(e)

        return id


    def getUserPayroll(self) -> List[dict]:
        """
        Returns a list of dicts of all the user information
        :return:
        """
        data = self.formattedData
        result = ""
        try:
            result = data["UserInfo"]
        except Exception as e:
            raise  Exception (e)
        return result
    
    
    
    
    
# if __name__ == '__main__':
#     aps_database = database()
#     aps_databseFile = "..\APS_Database.json"
#     aps_database.loadDatabase(aps_databseFile)
#
#     print(aps_database.checkUsernameAndPassword("taiye", "jebutu"))
#     print(aps_database.getUserID("taiye"))
#
#     user_database = database()
#     userFile = f"..\{aps_database.getUserID('taiye')}.json"
#     user_database.loadDatabase(userFile)
#
#     print(user_database.getUserPayroll())

