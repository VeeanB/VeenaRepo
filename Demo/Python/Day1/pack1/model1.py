def add(n1,n2):
    print("add in model1",n1+n2)

def multiply(n1,n2):
    print("multiply in model1",n1*n2)
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