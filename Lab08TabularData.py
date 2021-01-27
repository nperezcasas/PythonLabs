# Lab 8
# Printing tabular data
# Nuria Perez Casas

# Create a list to hold information about 10 cars
# Each entry in the list will have the following properties
#   Make
#   Model
#   Color (string with full color, e.g. "Blue")
#   Price (integer only)
#   Sale Discount (if any) (integer only)

def main():
    
    # We will print all the different options up here in the top and we
    # create a list that will later contain all the dictionaries

    print("|{:^11}|{:^15}|{:^11}|{:^11}|{:^11}|{:^11}"
          .format("Make","Model","Color Code","Price","Discount","Total Price"))
    print("|{:-^11}|{:-^15}|{:-^11}|{:-^11}|{:-^11}|{:-^11}"
          .format("","","","","",""))

    cars = []

    # We create all the dictionaries with all the different cars
    # and we add them to the list

    car_1 = {}
    car_1['make'] = "Buick"
    car_1['model'] = "Roadmaster"
    car_1['color'] = "Blue"
    car_1['price'] = 10000
    car_1['discount'] = 500

    cars.append(car_1)

    car_2 = {}
    car_2['make'] = "Ford"
    car_2['model'] = "F-150"
    car_2['color'] = "Grey"
    car_2['price'] = 27897
    car_2['discount'] = 1000

    cars.append(car_2)

    car_3 = {}
    car_3['make'] = "Jeep"
    car_3['model'] = "Wrangler"
    car_3['color'] = "White"
    car_3['price'] = 32260
    car_3['discount'] = 500

    cars.append(car_3)

    car_4 = {}
    car_4['make'] = "Tesla"
    car_4['model'] = "Model S"
    car_4['color'] = "Grey"
    car_4['price'] = 86200
    car_4['discount'] = 0

    cars.append(car_4)

    car_5 = {}
    car_5['make'] = "BMW"
    car_5['model'] = "740 1999"
    car_5['color'] = "Red"
    car_5['price'] = 3000
    car_5['discount'] = 100

    cars.append(car_5)

    car_6 = {}
    car_6['make'] = "Ford"
    car_6['model'] = "Mustang Coupe"
    car_6['color'] = "Black"
    car_6['price'] = 20600
    car_6['discount'] = 200

    cars.append(car_6)

    car_7 = {}
    car_7['make'] = "Chevrolet"
    car_7['model'] = "Camaro"
    car_7['color'] = "Yellow"
    car_7['price'] = 25000
    car_7['discount'] = 1000

    cars.append(car_7)

    car_8 = {}
    car_8['make'] = "Mazda"
    car_8['model'] = "Miata"
    car_8['color'] = "Red"
    car_8['price'] = 23000
    car_8['discount'] = 500

    cars.append(car_8)

    car_9 = {}
    car_9['make'] = "DeLorean"
    car_9['model'] = "DMC-12"
    car_9['color'] = "Grey"
    car_9['price'] = 44000
    car_9['discount'] = 750

    cars.append(car_9)

    car_10 = {}
    car_10['make'] = "Dodge"
    car_10['model'] = "Caravan"
    car_10['color'] = "Blue"
    car_10['price'] = 5400
    car_10['discount'] = 199

    cars.append(car_10)

    # Now we use the string formatting tools to align all the data in a simple table.

    for car in cars:
        print("|{:>11}|{:15}|{:11}|${:>10.2f}|-${:>8.2f}|${:>10.2f}"
              .format(car['make'], car['model'], car['color'].upper()[:3], car['price'], car['discount'],car['price']-car['discount']))

if __name__ == "__main__":
    main()

# For example, you might have a Blue Buick Roadmaster that is $10,000,
# with a current sale going for $500 off.

# Once you have this data structure that contains at least 10 cars,
# print out the data in a tabular format:

# Make  Model       Color Code  Price       Discount    Total Price
# Buick Roadmaster  BLU         $10,000.00  -$  500.00  $9,500.00
#  Fake Fakecar	    RED		$ 5,000.00  -$1,000.00  $4,000.00

# The make should be right-aligned and the model left-aligned.
# The color code is the first three letters of the full color, capitalized.
# Prices should have all dollar signs aligned, and all decimal points aligned
        
