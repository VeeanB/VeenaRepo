fw=open("test.txt","w")
fw.write("Veena1\n")
fw.write("Python\n")
fw.write("Course\n")
fw.write("Selenium\n")
fw.close()
fr=open("test.txt")
lines = fr.readlines()
fr=open("test.txt","w")
for line in lines:
    print(line[::-1])
    line1=line.strip("\n")
    #print(line1)
    fr.write(line[::-1])


# with open("test.txt") as fh:
#     lines = fh.readlines()
#
# with open("test.txt","w") as fw:
#     print(lines)
#     for line in lines:
#         #print(line[::-1])
#         line1=line.strip("\n")
#         print(line1)
#         fw.write(line1[::-1])


#Seek file
#copy
#delete
#Rename
#move path files    