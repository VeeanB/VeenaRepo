#from TestCases.Test_Login import Test_Suit_Login
import configparser

con_ob= configparser.RawConfigParser()
con_ob.read(r"C:\Users\veenu\PycharmProjects\PythonClass\selenium\Practice_PyTestFrame\Configuration\config.ini")

class ReadConfig:
    @staticmethod
    def GetBaseURL():
        return con_ob.get("common data","base_url")
    @staticmethod
    def GetUsername():
        return  con_ob.get("user data","username")
    @staticmethod
    def GetPassword():
        return con_ob.get("user data","password")


