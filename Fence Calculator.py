# Fence cost calculator
# Author: Josh
  
# Here is where we def the function Valid_num
# This function checks whether the user's input is valid

def valid_num(question):
    error = "Woops, that is not a valid float number."
    while True:
        try:
            response = float(input(question)) # response is a varible that stores the users input that can be a float number.
            if response > 0:
                return response
            
            else:
                print(error) # Print the variable which stores the error message
        except ValueError:
            print(error)
  
keep_going = "" 
while keep_going == "": # While the variable, keep_going, stores "", run the main script
    print("\nWelcome to my Fence Cost Calculator!\nEnter in the width and length of the area bellow.\nNext, enter the cost of fencing per meter")

    width = valid_num("What is the width: ") # Questions that store the users input after running it through the func, valid_num
    length = valid_num("What is the hight: ")
    cost = valid_num("What is the price per m?")

    perimeter = 2 * (width + length) # The variables that store the user's width and length, are added together then squared
    print(f"The perimeter is {perimeter}")

    price_of_fencing = perimeter * cost # The price of the fencing is the user's perimeter times the cost
    print(f"The cost of fencing is {price_of_fencing}")
    keep_going = input("\nPress <enter> to keep going. Press <any> to quit\n")

print("Thank you for using my Fence Cost Calculator")
