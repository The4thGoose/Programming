# Kyle Wenzel
# September 25, 2020
# Program3 Program
# This program will 
# Variable list: 
#   var1 - description
#   var2 - description

print("Welcome to the Progam3 Program\n")

# Step 1: 
amount = float(input("What is the cost of your meal? "))

tip15 = float(amount * 0.15)
tip20 = float(amount * 0.2)

final15 = amount + tip15
final20 = amount + tip20

print("{:}${:.2f}".format("\nYour amount before tip was: ", amount))
print("")
print("{:}${:.2f}".format("Your amount with 15% tip is: ", final15))
print("{:}${:.2f}".format("\tAmount tipped: ", tip15))
print("")
print("{:}${:.2f}".format("Your amount with 20% tip is: ", final20))
print("{:}${:.2f}".format("\tAmount tipped: ", tip20))

# Step : Wait for escape keystroke
input("\nPress enter to exit...")