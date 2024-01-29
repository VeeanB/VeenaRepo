color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])
exam_st_date = (11, 12, 2014)

print("The examination will start from : %i / %i / %i" % exam_st_date)

a = int(input("Input an integer: "))

# Create new integers 'n1', 'n2', and 'n3' by concatenating 'a' with itself one, two, and three times, respectively
n1 = int("%s" % a)          # Convert 'a' to an integer
n2 = int("%s%s" % (a, a))   # Concatenate 'a' with itself and convert to an integer
n3 = int("%s%s%s" % (a, a, a))  # Concatenate 'a' with itself twice and convert to an integer

# Import the 'calendar' module
import calendar

# Prompt the user to input the year and month
y = int(input("Input the year : "))
m = int(input("Input the month : "))

# Print the calendar for the specified year and month
print(calendar.month(y, m))

