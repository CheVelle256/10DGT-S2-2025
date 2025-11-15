# Ultimate Conversion Calculator
# Author: Josh
# Version 1

def valid_num(question): #Defines a error checking func that checks if the users input is valid
    error = "Woops, that is not a valid number."
    while True:
        try:
            response = float(input(question).strip().lower())
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def get_conversion_type(question): # Defines a error checking func that checks if the users input is a valid conversion type
   error = "Invalid type. Please choose again.\n"
   while True:
        conversion_type = input(question).strip().lower() # Stores the users input, strips the white-space, then converts users input to lowercase.
        if conversion_type == "distance": # If the str returned from the line above == either distance, mass, time, volume, set the variable, distance_units to that str.
            return distance_units
        elif conversion_type == "mass":
            return mass_units
        elif conversion_type == "time":
            return time_units
        elif conversion_type == "volume":
            return volume_units
        print(error)

def get_unit(question, units): # Defines a error checking func that checks if the users input is a valid unit.
        while True:
            unit = input(question).strip().lower() # Unit stores the users input, strips WS and converts to lower.
            if unit in units: # if the response from unit is in the variable units
                return unit
            print(f"Invalid unit. Choose from: {avaliable_units}\n") # refers to line 73 which defines the var, avaliable_units, as the dict keys sepperated by, ", "

# Dictionaries for each conversion type
distance_units = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000
}

mass_units = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000
}

time_units = {
    "s": 1,
    "min": 60,
    "h": 3600
}

volume_units = {
    "ml": 0.001,
    "l": 1
}

user_name = input("Please enter your name: ")

# Main program loop
keep_going = "" 
while keep_going == "": # While the variable, keep_going, stores "", run the main script
    
    print(f"\nHello {user_name}\nWelcome to The Ultimate Conversion Calculator!")
    
    units = get_conversion_type("Choose a type: distance, mass, time, volume: ") # the units var, is run through the, get_conversion_type funct, then is set to the correct dict
    
    avaliable_units = ', '.join(units.keys()) # Avaliable_units = the keys (left side) of the selected dict of the var, conversion_type,  which are then seperated with ", " 
    print(f"\nAvailable units: {avaliable_units}")
    value = valid_num("\nEnter the amount to convert: ")
    from_unit = get_unit("Convert from: ", units) # the users input is run throught the funct, get_unit, and checks whether input is in the var units
    to_unit = get_unit("Convert to: ", units)

   


    value_to_base = value * units[from_unit]
    converted_value = value_to_base / units[to_unit]

    print(f"\nThe conversion:\n{value} {from_unit} = {converted_value} {to_unit}")
    keep_going = input("\nPress <enter> to keep going or any key to quit: ")

print("Thanks for using my Ultimate Conversion Calculator!")

