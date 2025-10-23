#Coffe Program
#Creating an input system for our coffee program
#Juergen Lier
#Date: 10/10/2025

# Version: 1
# TODO: Ask the user if they like coffee    

# Ask  the user whether they like coffee or not
'''like_coffee = input("Do you like coffee")
print(f'Your answer was "{like_coffee}".')
if like_coffee == "yes" or "Yes":
    print("This is great! I like coffee too.")
else:
    print("you are missing out! Why not give it a try?")'''
# Version 2
# While loop
'''keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee")
    
    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee == "y" or like_coffee == "Y":
        print("This is great! I like coffee too.")
        keep_going = "finished"
    
    elif like_coffee == "no" or like_coffee == "No" or like_coffee == "N" or like_coffee == "n":    
        print("you are missing out! Why not give it a try?")
        keep_going = "finished"
        
    else:
        print("I don't understand")'''


# Version 3
# Making the program more Pythonic
'''keep_going = ""
while keep_going == "":
    # Convert answer to lower case using .lower
    like_coffee = input("Do you like coffee?\n"). lower()
    if like_coffee == "yes" or like_coffee == "y":
        print("That's great I like coffee too")
    
    elif like_coffee == "no" or like_coffee or like_coffee == "n":
        print("You are missing out! Why not give it a try?")
        
        like_tea = input("Do you like tea insted?").upper()
        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee another try :)")
        
        elif like_tea == "NO" or like_tea == "N":
            print("I am sorry. Thats all I have for now.")
        
        else:
            print("I dont understand please answer with either Yes or No")
            
    else:
            print("I dont understand please answer with either Yes or No")
    
    keep_going = input("press <ENTER> to continue, or any other key to quit. Thanks!\n")'''
    
# Code that tests whether a vailid input iss given (v1.4)
# Use the function parameters to make my code more pythonuc.
    
def valid_num(question, low, high):
    error = f"Woops, that is not an interger between {low} and {high}."
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                break # This ends the loop
            
            else:
                print(f"{error}\n")
        except ValueError:
            print(error)
    return response # This makes the response available toe be used

if __name__ == "__main__":
    num_1 = valid_num("Enter a number between 1 - 10:", 1,10)
    print(f"You entered {num_1}\n")

    num_2 = valid_num("Enter a number between 15 - 25:",15,25)
    print(f"You entered {num_2}\n")

    num_3 = valid_num("Enter a number between 30 - 45:",30,45)
    print(f"You entered {num_3}\n")

    num_4 = valid_num("Enter a number between 50 - 65:",50,65)
    print(f"You entered {num_4}\n")

    multiply = num_1 * num_2 * num_3 * num_4
    print(f"Your three numbers multiplied together are equal to {multiply}\n")

    sum = num_1 + num_2 + num_3
    print(f"The total of {num_1}, {num_2} and {num_3} is {sum}.\n")