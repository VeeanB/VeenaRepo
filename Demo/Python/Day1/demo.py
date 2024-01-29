class myclass:
    a=10
    b=20
    #alist =list[10,20,30,40]
    sum=0
    def myfunc(self):
        print("Inside the myfunc")
        #for i in alist
        sum=a+b
        print(sum)
        return sum


obj=myclass()
obj.myfunc()
for num in range(-2,-5,-1):
    print(num, end=", ")