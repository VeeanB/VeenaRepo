class parent1:

     @classmethod
     def func1(cls,a):
         a = "parent1 variable_class"
         parent1.a=a
         print("class method parent1")

     @staticmethod
     def func2(a):
         print("static method parent1")

class parent2:

     @classmethod
     def func1(cls,a):
         a = "parent2 variable_class"
         parent2.a=a
         print("class method parent2")

     @staticmethod
     def func2(a):
         a="parent2 variable_static"
         parent2.a=a
         print(a)
         print("static method parent2")

class child(parent2,parent1):
    a = "child variable"
    def myfunc(self):
         print("instance method child")

         parent1.func1(10)
         parent1.func2(20)
         parent2.func1(30)
         parent2.func1(40)
         print(self.a)
         print(parent1.a)
         print(parent2.a)






obj=child()
obj.func2(10)
child.func2(10)
obj.func1(10)
child.func1(30)
obj.myfunc()









# class a():
#     var1 = 0
#     var2 = {}
#     def print_var(self):
#         print(self.var1)
#         print(self.var2)
#
# class b(a):
#     @classmethod
#     def modify_var(cls):
#         cls.var1 = 1
#         cls.var2['temp']="something"
#
# o1 = a()
# o2 = b()
# print("Initial Values")
# o1.print_var()
# o2.print_var()
# print("Changing Values")
# o2.modify_var()
# print("Print values after change")
# o1.print_var()
# o2.print_var()