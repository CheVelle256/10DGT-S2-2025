# Error checking 
# Author: Josh
# Date 22/10/2025
# Version 1

#Code that tests whether a valid input is given (v.1)
'''done = False # Boolean variable set to False
while not done:
    num = int(input("Please enter your value"))
    done = True
    
print(f"The number you entered is {num}")'''

#Code that tests whether a valid input is given (v1.1)
# Use the try and except method to catch errors
'''done = False
while not done:
    try: #This method tries for a valid input
        num = int(input("Please enter a number: "))
        done = True
        
    except ValueError:
        print("That is not a valid float number. \n")

print(f"The number you entered is {num}")'''
    
# Code that tests whether a valid input is given (v1.2)
# Create a function to call everytime I ask the  user for a nummber .A 
# A function is a chunk of code that does something
# Functions can be used over and over again.
# To use a function (call it), write out its name with parantheses at the end
# To create a function. strat with the word def


'''def test_int_num():
    done = False
    while not done:
        try: #This method tries for a valid input
            num = int(input("Please enter a number: "))
            done = True
            
        except ValueError:
            print("That is not a valid float number. \n")

    print(f"The number you entered is {num}.")
    
# Main routine 
test_int_num() # This calls the function so that we can use it'''

#cODE THAT TESTS WHETHER A VALID INPUT IS GIVEN (v1.3)
#USE THE FUNCTION PARAMETERS

def test_int(question): # 'question' is a placeholder
    done = False
    while not done:
        error = "That is not a valid number"
        print(question)
        try: #This method tries for a valid input
            num = int(input())
            done = True
            
        except ValueError:
            print(error)

    return(num) # gives back the value of num so that I can use it outside of the function.
    
    
# Main routine
num1 = test_int("please enter your first number:")
print(f"Your first number you entered is {num1}")

num2 = test_int('Please enter your second number:')
print(f"The second number you entered is {num2}")

sum = num1 + num2
print(f"Your numbers added together equal to {sum}")
    