# Nuria Perez Casas
# COMS 103
# Lab 4

# Welcome to the converters program. This one is really similar to
# the last one we did but this time we are going to ask the user
# what conversion they want to make.


# We will use all the functions that we already made for the last lab
# but now we will establish a parameter and we will change print for
# return.

# Also this time we won't ask the input all at the end as well, so
# we don't need the imput statement anymore. We will only use 1 input()
# statement and it will be in the main loop. 

def inches_to_centimeters(inches):
    """This function converts from inches to centimeters
    Parameter:
        inches - the number of inches to convert"""
    
    centimeters = inches * 2.54
    return centimeters

def centimeters_to_inches(centimeters):
    """This function is the opposite from the previous one. It converts
    from centimeters to inches.
    Parameter:
        centimeter - the number of centimeters to convert
    I found the conversion online that 1 inch is 0.39 times
    a centimeter."""
    
    inches = centimeters * 0.393701
    return inches

def liters_to_gallons(liters):
    """This function transforms liters to gallons.
    Parameter:
        liters - the number of liters to convert
    I found the conversion online that 1 gallon is 0.264172
    times a liter."""
    
    gallons = liters * 0.264172
    return gallons

def gallons_to_liters(gallons):
    """This function is the opposite from the previous one. It converts
    from gallons to liters.
    Parameter:
        gallons - the number of gallons to convert
    I found the conversion online that 1 liter is 3.78541 times a gallon.
    """
    
    liters = gallons * 3.78541 
    return liters
                  
def meters_to_yards(meters):
    """This function transforms meters to yards.
    Parameter:
        meters - the number of meters to convert
    I found the conversion online that 1 yard is 1.09361
    times a meter.
    """
    
    yards = meters * 1.09361
    return yards

def yards_to_meters(yards):
    """This function is the opposite from the previous one.
    It converts from yards to meters.
    Parameter:
        yards - the number of yards to convert
    I found the conversion online that 1 meter is 0.9144
    times a yard.
    """
    
    meters = yards * 0.9144
    return meters

def kilograms_to_pounds(kilograms):
    """This function transforms kilograms to pounds.
    Parameter:
        kilograms - the number of kilograms to convert
    I found the conversion online that 1 pound is 2.20462
    times a kilogram.
    """
    
    pounds = kilograms * 2.20462
    return pounds

def pounds_to_kilograms(pounds):
    """This function is the opposite from the previous one.
    It converts from pounds to kilograms.
    Parameter:
        pounds - the number of pounds to convert
    I found the conversion online that 1 kilogram is 0.453592
    times a pound.
    """
    
    kilograms = pounds * 0.453592
    return kilograms                

def fahrenheit_to_celsius(fahrenheit):
    """This function transforms fahrenheit to celsius.
    Parameter:
        fahrenheit - the number of fahrenheit to convert
    I found the conversion online that to transfrom fahrenheit to
    celsius we need a formula: celsius = (fahrenheit - 32) % 1.8
    """
    
    celsius = (fahrenheit - 32) % 1.8
    return celsius             

def celsius_to_fahrenheit(celsius):
    """This function is the opposite from the previous one, it
    transforms celsius to fahrenheit.
    Parameter:
        celsius - the number of celsius to convert
    I found the conversion online that to transfrom celsius to
    fahrenheit we need the formula: fahrenheit = celsius * 1.8 + 32
    """
    
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit    
                 
# This time instead of using a demo function we will use a main() and
# we will create a loop, so that the program runs over and over again
# asking the user for it's conversions

def main():
    
    print("WELCOME to the CONVERTERS program.")
    print()
    print("Here you will be able to make some conversions!")
    print("It is really simple, type the conversion you want to make,")
    print("and the program will guide you to instantly get the result")
    print()

    # We print all the conversions we have so that the user knows
    # what the program can do. And we ask the user what type of value
    # he wishes to convert.

    # I know we were supposed to put the list of conversions over and over
    # but I thought the program looked less messy if we just put the list
    # once at the beginning. 
    
    print("This is the list of conversions you can make:")
    print()
    print("[inches] (to centimeters)")
    print("[centimeters] (to inches)")
    print("[liters] (to gallons)")
    print("[gallons] (to liters)")
    print("[meters] (to yards)")
    print("[yards] (to meters)")
    print("[kilograms] (to pounds)")
    print("[pounds] (to kilograms)")
    print("[fahrenheit] (to celsius)")
    print("[celsius] (to fahrenheit)")
    print()

    # Here is the beginning of the loop. We start it now because
    # we don't want the welcome message to repeat over and over.

    while True:
        
        starting_unit = input("Enter the type of value you wish to convert: ")

    # As we said, it will ask the input only one time using the value
    # to get a result and using the starting unit so that the user knows
    # what we are asking. 

        value = int(input("How many " + starting_unit + "? "))

    # Now we use if and elif's to call the program the user will ask.
    # Again this time we optimize things and we will print only the result
    # with the value. 

        if starting_unit == "inches":
            result = inches_to_centimeters(value)
        elif starting_unit == "centimeters":
            result = centimeters_to_inches(value)
        elif starting_unit == "liters":
            result = liters_to_gallons(value)
        elif starting_unit == "gallons":
            result = gallons_to_liters(value)
        elif starting_unit == "meters":
            result = meters_to_yards(value)
        elif starting_unit == "yards":
            result = yards_to_meters(value)
        elif starting_unit == "kilograms":
            result = kilograms_to_pounds(value)
        elif starting_unit == "pounds":
            result = pounds_to_kilograms(value)
        elif starting_unit == "fahrenheit":
            result = fahrenheit_to_celsius(value)
        elif starting_unit == "celsius":
            result = celsius_to_fahrenheit(value)

        print(result)
        print()



if __name__ == "__main__":
    main()

# Hope you enjoy the program!! :)

