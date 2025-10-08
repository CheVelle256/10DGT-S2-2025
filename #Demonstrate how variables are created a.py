#Demonstrate how variables are created and how they work
#Author: Joshua Angus
#Date:19-09-2025
#Version 1.0

#Different types of variables
#Store a string
greeting = "Hello World"
print(greeting)

#Store a number
my_number = 80 # Assigned 80 to: my_number
print(my_number)

my_number2 = 7 
print(my_number2)

# Assign the value of one variable to another
my_number = greeting
print(my_number) # Dont assign values to variables that dont make sense

'''Do calculations with variables and store the result in another variable.
With comments, i can now 
press enter
as
many
times
as 
I
LIKE'''

# Creating new variable
num_1 = 5
num_2 = 18

sum1 = 5 + 18 # This not good practice
print(sum1)

sum1 = num_1 + num_2 # Use the Variables instead rather than using their values.
print(sum1)

sum_string1 = '18'
sum_string2 = "5"

# Adding two strings together. This is called concatenation
sum = sum_string1 + sum_string2
print(sum)

# Print formatting. "f" stands for "format" and inserts the value of variables
print(f"My calculation for adding {num_1} and {num_2} together is {sum1}.")