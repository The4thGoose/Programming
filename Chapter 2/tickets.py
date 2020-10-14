# Kyle Wenzel
# September 17, 2020
# Ticket Program
# This program will calculate the total ticket price based on the amount of tickets needed
# Variable list: 
#   ticket - number of tickets needed
#   price - price per ticket (15 dollars)
#   total - total cost for all tickets

print("Welcome to the Ticket Program\n")

# Step 1: Ask for number of tickets
ticket = float(input("How many tickets do you need? "))

# Step 2: calculate the cost
price = 15
total = ticket * price

# Step 3: Print the final cost
print("\nThe total cost for all the tickets are: ", "${:,.2f}".format(total))

# Step 4: Wait for escape keystroke
input("\nPress enter to exit...")