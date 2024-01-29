import selenium

print("hello")

a= 3
print (a)

Str = "Hello World"
print(Str)

b, c, d = 5, 6.4, "Great"
#print("Value is"+c)
print("{} {}".format("Value is", +c))
print(type((d)))
print(type((b)))
print(type((c)))
#print("Value is"+a)
#print("Value is"+d)
#Lists
a=[1,2,3,4,5,6]
print(a[1])
values = [1, 2, "first", 4, 5]

print(values[3])
print(values[2])
print(values[-1])
print(values[1:4])
values.insert(3, "name")
print(values)
values.append("Lastname")
print(values)
values[2]= "FIRST"
print(values)
del values[0]
print(values)
#tuple
tuple =(1 ,2 ,"Rahul", 3, 4)

print(tuple[2])

dict ={1: "Rahul", 2: "Shetty", "abc": 4}
print(dict["abc"])
print(dict[1])
print(dict[2])
#empty dictionary
dict = {}
dict["First Name"] = "Rahul"
dict["Last Name"] = "Shetty"
dict["Gender"] ="Male"
print(dict)

