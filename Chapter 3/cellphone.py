# Kyle Wenzel
# October 1st, 2020
# Cellphone Program
# This program will 
# Variable list: 
#   var1 - description
#   var2 - description

print("Welcome to the cellphone Program\n")

# Step 1: 
texts = int(input("How many texts were sent? "))

if texts <= 300:
    bill = 20
else:
    bill = 20 + (texts - 300) * 0.03

print("Your total bill is ${:,.2f}".format(bill))
# Step : Wait for escape keystroke
input("\nPress enter to exit...")