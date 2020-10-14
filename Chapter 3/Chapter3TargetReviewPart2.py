# Kyle Wenzel
# October 5th, 2020
# Chapter 3 Target Review Part 2 Program
# This program will 
# Variable list: 
#   var1 - description
#   var2 - description

print("Welcome to the Chapter 3 Target Review Part 2 Program\n")

# Step 1: 
total = float(input("What is the total of your order?"))

if total < 100:
    shipping = "$10 Regular Shipping"
elif total >= 100 and total < 150:
    shipping = "$5 Rgular Shipping"
elif total >= 150 and total < 200:
    shipping = "Free 2-3 Day Shipping"
elif total >= 200: 
    shipping = "Free Overnight Shipping"

print("\nThe shipping for your order is")
print(shipping)

# Step : Wait for escape keystroke
input("\nPress enter to exit...")