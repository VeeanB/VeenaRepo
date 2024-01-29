a="global varible"
class myclass:
    a="class variable"
    def __init__(self):
        print("______________Inside the constructor__________________")
        a="constructor variable"

        print(f"constructor variable {a}")
        print(f"class varible{myclass.a}")
        print(f"globale varible{globals()['a']}")
        self.a = a
        #myclass.a = a

    def inistancemethod(self):
        print(f"constructor variable {self.a}")
        print(f"class variable {myclass.a}")
        print(f"global variable {a}")


    @staticmethod
    def staticmethod():
        print(f"constructor variable {myclass.a}")
        print(f"class variable {myclass.a}")
        print(f"global variable {a}")

    @classmethod
    def classmethod(cls):
        print(f"constructor variable {cls.a}")
        print(f"class variable {myclass.a}")
        print(f"global variable {a}")






obj = myclass()
print("________________Inside instance method______________________")

obj.inistancemethod()
print("_______________Inside the static method_____________________")

obj.staticmethod()
print("_______________Inside the class method______________________")

obj.classmethod()
