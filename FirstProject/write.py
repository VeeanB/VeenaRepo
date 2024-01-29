#file = open('test.txt')
#file.close()

#read the file and store line in the list
#reverse list
#write back to text file
with open('test.txt','r') as reader: # closing and opening file
    content = reader.readlines() #intial list from file
    reversed(content) #reversing list from file
with open('test.txt', 'w') as writer:
    for line in reversed(content):
        writer.write(line)