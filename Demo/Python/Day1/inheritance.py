class Parent:
    def fun_1(self):
      print("Parent class")
class child1(Parent):
    def fun_2(self):
      print("Child 1 class")
class child2(Parent):
    def fun_3(self):
     print("child 2 class")
class child3(child2):
    def fun_4(self):

     print("child 3 class")
obj = child3()
obj.fun_1()
obj1=child3()
obj1.fun_4()
obj1.fun_3()

#Static method is a general utility method that performs a task in isolation. This method doesn’t have access to the instance and class variable.


class myclass:

    def __init__(self):
        a = 10
        print(f"a is instance variable{a}")


obj = myclass