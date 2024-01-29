class Parent1:
    a="Parent1 variable"
    def func1(self):
        print("Inside the parent1 class method")
    def A(self):
        print("Calling same methode(A) in side the parent1 method")

class Parent2:
    a="Parent2 variable"
    def func2(self):
        print("Inside the parent 2 class method ")
    def A(self):
        print("Calling same methode(A) in side the parent2 method")
class child(Parent2,Parent1):
    a="Child variable"
    def child_function(self):
        print("Inside the child class method")


    # def A(self): #RecursionError: maximum recursion depth exceeded while calling a Python object
    #     print("this is func_child1")
    #     print("Calling same methode(A) in side the child method")
    #     print(self.a)
    #     print(super().a)
    #     self.A()
    #     super().A()
    #     Parent1().a
    #     Parent1().A()
    def A(self):
        print("Child class method")
        print(self.a)
        print(super().A())
        print(super().a)
        print(Parent1().a)
        print(Parent2().a)
        print(Parent1().A())
        print(Parent2().A())


obj=child()
print(obj.a)
print(obj.A())
obj.func2()
obj.func1()
obj.child_function()


