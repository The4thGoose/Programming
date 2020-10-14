# Kyle Wenzel
# September 21st, 2020
# Mileage Program
# This program will ask for car, tank size, miles per gallon, and cost of gallon and calculates how far and how much a tank of gas will go
# Variable list: 
#   car - car brand
#   size - tank size
#   mpg - miles per gallon
#   cpg - cost per gallon
#   distance - how far you can go on a tank of gas
#   cpt - cost per tank

print("Welcome to the Mileage Program\n")

# Step 1: Ask for car model
car = input("What is the brand of your car? ")

# Step 2: Ask for tank size
size = float(input("What is the size of the tank in your " + car + " (in gallons)? "))

# Step 3: Ask the miles per gallon for the car
mpg = float(input("How many miles per gallon does your " + car + " get? "))

# Step 4: Ask for cost of a gallon
cpg = float(input("What is the cost for a gallon of gas? "))

# Step 5: calculate how far you can go on a tank
distance = mpg * size

# Step 6: calculate cost to fill tank
cpt = cpg * size

# Step 7: print cpt and distance
print("\nA brand new", car, "can travel", distance, "miles on one tank of gas.")
print("\n{:}${:.2f}{:}{:}".format("It will cost ", cpt, " to fill the tank in your ", car + "."))
# Step : Wait for escape keystroke
input("\nPress enter to exit...")