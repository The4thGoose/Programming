# Kyle Wenzel
# January 12th, 2021
# Chapter 5 Test

# Import Modules
import os
import time

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Print welcome message, wait 5 seconds, then clear terminal
print("Welcome to the chapter 5 test. ")
time.sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')

# Define Variables
ticker = 0
total = 0
average = 0
vsb = [("Gorthi", 11915.98), 
    ("Nathan", 13344.43), 
    ("DeMare", 10773.62), 
    ("Columbus", 23166.84)]

# Keep adding users until the user doesn't want to anymore
selection = "y"
while selection.lower() == "y" or selection.lower() == "yes":
    # Ask for input and append it
    selection = input("Would you like to add a person to the list (y/n)? ")
    if selection.lower() == "y" or selection.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("What is the new person's name? ")
        money = float(input("\nWhat is the amount of sales for that employee? "))
        appending = name, money
        vsb.append(appending)
    os.system('cls' if os.name == 'nt' else 'clear')

# Create a total for the average
for entry in vsb:
    a, b = entry
    total += b
    ticker += 1

# Calculate Average
average = total / ticker

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Print List Header
print("{:<15}{:<15}".format("Name", "Total"))
print("-"*30)

# Print List
for entry in vsb:
    a, b = entry
    print("{:<15}${:<15,.2f}".format(a, b))

# Print Total
print("")
print("{:<15}${:<15,.2f}".format("Total", total))

# Print Average
print("{:<15}${:<15,.2f}".format("Average", average))

input("\nPress enter to exit...")
os.system('cls' if os.name == 'nt' else 'clear')