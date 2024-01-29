mylist=[10,20,30,40]
print(mylist)
print(mylist[0])
print(mylist[::-1])
print(mylist[::-2])
print(mylist[::-3])
print("-2 values")
print(mylist[0:-3])
print("******tuple********")
mytuple=("Veena","Ramesh","Pranavi","Pranathi")
print(mytuple)
print(mytuple[::-1])
print(mytuple[2:3])
print(mytuple[2:-2])
print("******set********")
myset={10,20,30,40}
print(myset)
myset=list(myset)
print(myset[::-1])
print("**************dictionary***********")
mydict={"name": "Veena","age": 29,"Quln": "BE"}
print(mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(mydict["name"])
mydict["name"]="XYZ"
print(mydict)
mydict.update({"Job":"ENG"})
print(mydict)
mydict1=mydict
print(mydict1)
mydict2=mydict.copy()
print(mydict2)
#mydict.pop("name")
#print(mydict)
#mydict.clear()
#print(mydict)



#mydict.__delitem__("name")
#print(mydict)
#del mydict["age"]
#print(mydict)
#del mydict
#print(mydict)
del mydict["age"]
print(mydict)
#del mydict
#print(mydict)
for i in mydict:
    print(mydict[i])
print("name" in mydict.keys())
print("XYZ" in mydict.values())
print("##########################################################")
list1 = list((1,2,3,4,5))
tuple1=tuple((6,7,8,9,10))
set1=set(("x","y","z"))
dict1=dict(name= "Veena",age=29)
frozenset1=frozenset(("apple","banana","Kiwi"))
print(list1)
print(type(list1))
print(list1[1:-2])
print(tuple1)
print(type(tuple1))
print(tuple1[1:-2])
print(set1)
print(type(set1))
print(dict1)
print(type(dict1))
print(frozenset1)
print(type(frozenset1))
print(type(0xFF))
print(type([]) is list)
print(type(range(5)))
print(type({}) is dict)
print(2 * 3 ** 3 * 4)
print(2%6)
print(-18 // 4)
print(2 ** 3 ** 2)
x = 100
y = 50
print(x and y)
a = 4
b = 11
print(a | b)
print(a >> 2)
x = 6
y = 2
print(x ** y)
print(x // y)

print(0b101)
print(0o10)
print(0x1F)
print(abs(-45.300))
print(int(2.999))
import math
print(math.ceil(252.4))
print(math.floor(252.4))
from numbers import Number
from decimal import Decimal
from fractions import Fraction

print(isinstance(2.0, Number))
print(isinstance(Decimal('2.0'), Number))
print(isinstance(Fraction(2, 1), Number))
print(isinstance("2", Number))
print( (1.1 + 2.2) == 3.3 )
print(round(100.2563, 3))
print(round(100.000056, 3))
strOne = str("pynative")
strTwo = "pynative"
print(strOne == strTwo)
print(strOne is strTwo)

str1 = "My salary is 7000";
str2 = "7000"
str1 = 'Welcome'
myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString)
print(stringList[1] is myString)
str = "my name is James bond";
print (str.capitalize())
str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count(sub, 4))
str = "My salary is 7000";
print(str.isalnum())
str1 = 'Welcome'
print(str1*2)

my_list =[10,20,20.5,'Python',100]
# It will print only datatype of variable

sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])

print(sampleList[-4:-1])
aList = [5, 10, 15, 25]
print(aList[::-2])
print("**************Doubt*************************************")
aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

list1 = ['Test', '123', 'PyTest']
print (max(list1))

mylist = [5, 17, 32, 14, 10, 21]

# Example 1: Using max() function
# Get the maximum value in the list
max_value = max(mylist)
print (min(mylist))
mylist = ["Python","C++","Java","Hadoop"]
print("Original list: ", mylist)

# Using max() to find the max value
max_value = max(mylist)
print("The largest string is:", max_value)
