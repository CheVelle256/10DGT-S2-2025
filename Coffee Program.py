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
keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee")
    
    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee == "y" or like_coffee == "Y":
        print("This is great! I like coffee too.")
    
    elif like_coffee == "no" or like_coffee == "No" or like_coffee == "N" or like_coffee == "n":    
        print("you are missing out! Why not give it a try?")
        