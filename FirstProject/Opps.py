    #Class are nothing but user defined blueprint or prtotype
#sum ,Multiplcation ,Addition,Constant
#Class will have methods,varibles,constructor etc
#Objects of classes
#self keywork is mandatory to calling the method variables
#constructor name is init
#Constructor are the nothing but its method in the class
#default constructor
class Calculator:
    num = 100
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
            print(self.firstNumber + self.secondNumber + Calculator.num)


obj = Calculator(2, 3)
obj.getData()
obj.Summation()
print("**************************")
obj1 = Calculator(4 , 5) #syntax to create object for class
print(obj1.Summation())


