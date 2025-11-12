# Area and Perimeter Script
# Version 1
# Author: Josh
 

def valid_num(question):
    error = "Woops, that is not a valid float number."
    while True:
        try:
            response = float(input(question))
            if response > 0:
                return response
            
            else:
                print(error)
        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
    print("\nWelcome to my Perimeter and Area Calculator!\nEnter in the width and height of your shape bellow.\n")
    
    width = valid_num("What is the width: ")
    hight = valid_num("What is the height: ")

    area = width * hight
    print(f"The area is {area}")

    perimeter = 2 * (width + hight)
    print(f"The perimeter is {perimeter}")

    keep_going = input("Press <enter> to keep going. Press <any> to quit\n")

print("Thank you for using my Area and Perimeter Calculator\n")