def add(a,b):
    sum=0
    sum=a+b
    print(f"add {sum} in model2")
def mul(a,b):
    mul=0
    mul=a*b
    print(f"add {mul} in model2")
class myclass:
    a = "class varaible"
    def __init__(self):
        print("Constructor")
    def A(self):
        print("Function A is in Model2")

    @staticmethod
    def stat():
     print(f"staticmethod in model2{myclass.a} ")

    @classmethod
    def clas(cls):
        print(f"claas method in model2{myclass.a}")