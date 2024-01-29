class Parent1:

    def __init__(self):
        a="Instance varible in parenet1 class"
        Parent1.a=a
        print("Parent1 contructor")
    def A(self):
        print("Prining A method in ths Parent1 class")
class Parent2:
    def __init__(self):

        a="Instance varible in parenet2 class"
        Parent2.a=a
        print("Parent2 contructor")
    def A(self):
        print("Prining A method in ths Parent2 class")
class child(Parent1,Parent2):
    def __init__(self):
        a = "Instance varible in child class"
        child.a=a
        print("child contructor")

    def A(self):
        print("Prining A method in ths child class")
        print(child.a)
        super().A()
        print(Parent2.a)
        print(Parent1.a)

        Parent2.__init__(self)
        Parent1.__init__(self)
        Parent1()
        Parent2()

obj=child()
obj.A()

