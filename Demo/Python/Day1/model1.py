def add(a,b):
    sum=0
    sum=a+b
    print(f"add {sum}")
def mul(a,b):
    mul=0
    mul=a*b
    print(f"add {mul}")

class myclass:
    a= "class varaible"
    def __init__(self):
        print("Constructor")
    def A(self):
        print("Function A is in Model1")
    @staticmethod
    def stat():
        print(f"staticmethod in model1{myclass.a} ")
    @classmethod
    def clas(cls):
        print(f"claas method in model1{myclass.a}")
