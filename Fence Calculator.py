# Fence cost calculator
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
  
Keep_going = ""
while Keep_going == "":
    print("\nWelcome to my Fence Cost Calculator!\nEnter in the width and length of the area bellow.\nNext, enter the cost of fencing per meter")
    
    width = valid_num("What is the width: ")
    length = valid_num("What is the hight: ")
    cost = valid_num("What is the price per m?")
    
    perimeter = 2 * (width + length)
    print(f"The perimeter is {perimeter}")
    
    price_of_fencing = perimeter * cost 
    print(f"The cost of fencing is {price_of_fencing}")

    keep_going = input("Press <enter> to keep going. Press <any> to quit\n")

print("Thank you for using my Fence Cost Calculator")

