file = open('test.txt')
#Read all the content of file
#print(file.read(5)) # limited character
#read one single line using readline method
#print(file.readline())
#print(file.readline())


#print line by line using readline method in case 100line
#line = file.readline()
#while line!= "":
 #   print(line)
  #  line = file.readline()

#values =[abc, bvsdf,"cat", dog]
for line in file.readlines():
    print(line)


file.close()