# Kyle Wenzel
# September 17, 2020
# College Program
# This program will ask what school you want to attend
# Variable list: 
#   var1 - description
#   var2 - description

print("Welcome to the College Program\n")

# Step 1: 
college = input("What college do you want to attend? ")

# Step 2: 
tuition = float(input("What is the tuition at " + college + "? "))

# Step 3: 
rb = float(input("What is the cost for room and board at " + college + "? "))

# Step 4:
total = tuition + rb
total = float(total)
print("{:}{:}{:}{:.2f}".format("The the total for attending ", college, " is: ", total, "Dollars"))

# Step : Wait for escape keystroke
input("\nPress enter to exit...")