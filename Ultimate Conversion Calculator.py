# Ultimate Conversion Calculator
# Author: Josh
# Version 1

def valid_num(question):
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

def get_conversion_type(question):
   error = "Invalid type. Please choose again.\n"
   while True:
        conversion_type = input(question).strip().lower()
        if conversion_type == "distance":
            return distance_units
        elif conversion_type == "mass":
            return mass_units
        elif conversion_type == "time":
            return time_units
        elif conversion_type == "volume":
            return volume_units
        print(error)

def get_unit(question, units):
        while True:
            unit = input(question).strip().lower()
            if unit in units:
                return unit
            print(f"Invalid unit. Choose from: {avaliable_units}\n")

# Dictionaries for each conversion type (relative to base unit)
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
while keep_going == "":
    
    print(f"\nHello {user_name}\nWelcome to The Ultimate Conversion Calculator!")
    
    units = get_conversion_type("Choose a type: distance, mass, time, volume: ")
    
    avaliable_units = ', '.join(units.keys())
    print(f"\nAvailable units: {avaliable_units}")
    
    value = valid_num("\nEnter the amount to convert: ")
    from_unit = get_unit("Convert from: ", units)
    to_unit = get_unit("Convert to: ", units)
    
   
    

    value_to_base = value * units[from_unit]
    converted_value = value_to_base / units[to_unit]

    print(f"\nThe conversion:\n{value} {from_unit} = {converted_value} {to_unit}")
    keep_going = input("\nPress <enter> to keep going or any key to quit: ")

print("Thanks for using my Ultimate Conversion Calculator!")