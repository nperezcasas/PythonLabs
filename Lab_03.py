# Nuria Perez Casas
# COMS 103
# Lab 3

# Before we start we will introduce to the person that runs
# the program what is happening and what they should do

print("WELCOME to the 'CONVERTER DEMO' program. Type: demo() to start")

# We are going to create a function to be able to transform inches to
# centimeters a lot faster without having to type it all the time. 

def inches_to_centimeters():
    """This function converts from inches to centimeters"""
    inches = int(input("How many inches? "))
    centimeters = inches * 2.54
    print(centimeters)

# Now we will do that same process but with the rest of the convertors
# we need

def centimeters_to_inches():
    """This function is the opposite from the previous one. It converts
    from centimeters to inches.
    
    I found the conversion online that 1 inch is 0.39 times
    a centimeter."""
    centimeters = int(input("How many centimeters? "))
    inches = centimeters * 0.393701
    print(inches)

def liters_to_gallons():
    """This function transforms liters to gallons.

    I found the conversion online that 1 gallon is 0.264172
    times a liter."""
    liters = int(input("How many liters? "))
    gallons = liters * 0.264172
    print(gallons)

def gallons_to_liters():
    """This function is the opposite from the previous one. It converts
    from gallons to liters.
    
    I found the conversion online that 1 liter is 3.78541 times a gallon.
    """
    gallons = int(input("How many gallons? "))
    liters = gallons * 3.78541 
    print(liters)
                  
def meters_to_yards():
    """This function transforms meters to yards.

    I found the conversion online that 1 yard is 1.09361
    times a meter.
    """
    meters = int(input("How many meters? "))
    yards = meters * 1.09361
    print(yards)

def yards_to_meters():
    """This function is the opposite from the previous one.
    It converts from yards to meters.
    
    I found the conversion online that 1 meter is 0.9144
    times a yard.
    """
    yards = int(input("How many yards? "))
    meters = yards * 0.9144
    print(meters)

def kilograms_to_pounds():
    """This function transforms kilograms to pounds.

    I found the conversion online that 1 pound is 2.20462
    times a kilogram.
    """
    kilograms = int(input("How many kilograms? "))
    pounds = kilograms * 2.20462
    print(pounds)

def pounds_to_kilograms():
    """This function is the opposite from the previous one.
    It converts from pounds to kilograms.
    
    I found the conversion online that 1 kilogram is 0.453592
    times a pound.
    """
    pounds = int(input("How many pounds? "))
    kilograms = pounds * 0.453592
    print(kilograms)                

# When transforming temperature we have to be very careful because
# it is not a regular conversion and we will need a formula. 

def fahrenheit_to_celsius():
    """This function transforms fahrenheit to celsius.

    I found the conversion online that to transfrom fahrenheit to
    celsius we need a formula: celsius = (fahrenheit - 32) % 1.8
    """
    fahrenheit = int(input("How many fahrenheit degrees? "))
    celsius = (fahrenheit - 32) % 1.8
    print(celsius)             

def celsius_to_fahrenheit():
    """This function is the opposite from the previous one, it
    transforms celsius to fahrenheit.

    I found the conversion online that to transfrom celsius to
    fahrenheit we need the formula: fahrenheit = celsius * 1.8 + 32
    """
    celsius = int(input("How many celsius degrees? "))
    fahrenheit = celsius * 1.8 + 32
    print(fahrenheit)    
                 
# We will put everything under another function called demo so
# that by typing demo() we get asked for all the conversions. 

def demo():
    inches_to_centimeters()
    centimeters_to_inches()
    liters_to_gallons()
    gallons_to_liters()
    meters_to_yards()
    yards_to_meters()
    kilograms_to_pounds()
    pounds_to_kilograms()
    fahrenheit_to_celsius()
    celsius_to_fahrenheit()

# Hope you enjoy the program!! :)

