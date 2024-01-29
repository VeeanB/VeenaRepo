#if else condition
greeting = " Good Morning "
if greeting == " Morning ":

        print("Condition Matches")
        print("second line")
else:
    print("Condition do not match")
print("if else condition code is completed")

#For loop
obj = [2, 3, 4, 5, 6]
for i in obj:
    print(i*2)

#Sum of natural number 1+2+3+4+5 =15
addition = 0
for j in range(1,6): #range (i,J) -> to J-1 for(i=0:i<5:i++)
    addition = addition + j
    print(j)
print(addition)
print("********************************************************************************")
for k in range(1,10,5): #range (i,J) -> to J-1 for(i=0:i<5:i+2) no of itertion
    addition = addition + k
    print(k)
for m in range(6): #skippping first index

    print(m)