import configparser

con_obj = configparser.RawConfigParser()
con_obj.read(r".\Configurations\config.ini")

class ReadConfig:
    @staticmethod
    def GetBaseUrl():
        return con_obj.get("common data", "base_url")

    @staticmethod
    def GetUsername():
        return con_obj.get("user data", "username")

    @staticmethod
    def GetPassword():
        return con_obj.get("user data", "password")