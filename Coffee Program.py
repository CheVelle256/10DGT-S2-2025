#Coffe Program
#Creating an input system for our coffee program
#Juergen Lier
#Date: 10/10/2025

# Version: 1
# TODO: Ask the user if they like coffee    

# Ask  the user whether they like coffee or not
like_coffee = input("Do you like coffee")
print(f'Your answer was "{like_coffee}".')
if like_coffee == "yes" or "Yes":
    print("This is great! I like coffee too.")
else:
    print("you are missing out! Why not give it a try?")