# Kyle Wenzel
# September 14th, 2020
# Pizza Program
# This program will find the total cost of the pizzas
# Variable List: 
#   cost - the cost of 1 pizza
#   amount - the amount of pizzas being purchased
#   tip - the percentage of the tip for the driver
#   sub - the subtotal of the order
#   tipamount - amount tipped to the driver
#   total - total cost for the pizza order

# Step 1: Print Welcome message
print("Welcome to the Pizza Program \n")

# Step 2: Define variables
cost = 10
amount = 3
tip = .10

# Step 3: Calculate totals for the order
sub = cost * amount
tipamount = sub * tip
total = sub + tipamount

# Step 4: Print the final amount
print("The total cost of the pizzas with a 10% tip is: ${:.2f}".format(total))

# Step 5: Wait for exit keystroke

input("\nPress enter to exit...")