X=10
def myfunction1():

    #print("inside function before initiating var X", X)
    X=40
    print("Inside the functions")

myfunction1()

X=30
def myfunc():
     global X
     print("inside function before initiating var x", X) # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
     X=20
     print("inside function after initiating var x", X)
     return X
print(myfunc())

def myfun(a,b,c,d):

    print(a+b+c+d)

myfun(2,3,c=4,d=5)

###############################################################################################################
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a

result = outer_fun(5, 10)
print(result)

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="XYZ", salary=9000)


def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}
student.clear()
print(student)
####################################################################
#Dictionary keys must be immutable  True
#In Python, Dictionaries are immutable False

def outer_fun(a,d):
    print("Inside the outer fuction")
    def inner_fun(c,b):
        return c+b
    return inner_fun(a,d)
    #return a

print(outer_fun(2,3))

def fun(**kwargs):
    print("displaying the arguments")
    return (kwargs.values())
print(fun(a=2,b=3))
sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])
aList = [5, 10, 15, 25]
print(aList[::-2])

print(("*******************************************************************"))
resList = [x+y for x in [2, 3] for y in [2, 3]]
print(resList)

#[‘Hello Dear’, ‘Hello Bye’, ‘Good Dear’, ‘Good Bye’]

aList = ["VEeNa", [4, 8, 12, 16]]
print(aList[0][1])
print(aList[1][3])
str = "My salary is 7000";
print(str.isalnum())
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set3 = set2.difference(set1)
print(set3)
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}
print(set1.issubset(set2))
print(set2.issuperset(set1))
print("*****************************************************")
#aSet = {1, 'PYnative', ['abc', 'xyz'], True}
#print(aSet)

aSet = {1, 'PYnative', ('abc', 'xyz'), True}
print(aSet)
set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}

set3 = set1.union(set2)
print(set3)

sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.update(["Blue", "Green", "Red"])
print(sampleSet)
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set1.difference_update(set2)
print(set1)
print("##########################################################################")
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.discard("Orange")
print(sampleSet)
#del sampleSet ["Orange"]
#print(sampleSet)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

aTuple = (100,)
print(aTuple * 2)

aTuple = ("Orange")
print(type(aTuple))
#aTuple = (100, 200, 300, 400, 500)
#aTuple.pop(2)
#print(aTuple)


