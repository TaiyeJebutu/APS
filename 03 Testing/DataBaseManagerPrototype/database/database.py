import json


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
        pass


    def outData(self) -> str:
        """
        Returns the formatted data
        :return:
        """
        return self.formattedData



