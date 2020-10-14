# Kyle Wenzel
# September 30th, 2020
# iTunes Program
# This program will 
# Variable list: 
#   amount - the number of songs being purchased
#   var2 - description

print("Welcome to the iTunes Program\n")

# Step 1: 
amount = int(input("How many songs would you like to buy? "))

# Step 2: 
if amount < 6: 
    cps = 1.29
elif amount >= 6:
    cps = 0.99

total = amount * cps

# Step 3: 
print("{:}{:,}{:}${:,.2f}".format("\nYour total cost of the ", amount, " songs being purchased is ", total))

# Step : Wait for escape keystroke
input("\nPress enter to exit...")