a,b=10,20
class myclass:
# a,b=2,3
# def myfunction1(self):
 #    a,b=1,4
  #   print(f"printing the a & b values of local variable {a} {b}")
   #  print(f"printing the a & b values of local variable {myclass.a} {myclass.b}")
    # print(f"printing the a & b values of local variable {globals()['a']} {globals()['b']}")

 #@classmethod
 #def myfunc2(cls,a,b): ## a and b local variable
  #        print(f"local variable {a} {b}")
   #       print(f"class variable {cls.a} {cls.b}")
    #      print(f"class variable {myclass.a} {myclass.b}")

     #     print(f"global variable {globals()['a']} {globals()['b']}")

 #@staticmethod
 #def myfunct3(a,b):
  #   print(f"local variable {a} {b}")
   #  print(f"class variable {myclass.a} {myclass.b}")
    # print(f"class variable {globals()['a']} {globals()['b']}")


 def __init__(self):
    print("inside the the constructor")
 def __init__(self,a,b):
     #a,b=100,200
     print(f"parameterized constructor{a} , {b}")

 #def __init__(self):
  #    print("printing constructor1")

 #def __init__(self):
  #       print("printing constructor2")

 #def __init__(self):
  #       print("printing constructor3")



obj=myclass(2,3)
#obj.myfunction1()
#obj.myfunc2(2,3)
#obj.myfunct3(4,5)

