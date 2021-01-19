# Kyle Wenzel
# January 14th, 2021
# Final Project
# It's a cash register or something, IDK
# You will find the variable dictionary entries right above the respective variable's definition 

# imports modules
import os
import time
import random

# Var waitime: How long the program will wait to clear the console after displaying the welcome message
waitime = random.uniform(1, 2)
# Var valid: used to define if the order is over
valid = False
# Var menu: used to store the menu
menu = [["H", "Hamburger", 1.29], ["C", "Cheeseburger", 1.49], ["F", "Fries", 0.99], ["O", "Onion Rings", 1.09], ["S", "Small Soft Drink", 0.79], ["L", "Large Soft Drink", 1.19]]
# Var extramenu: used to store the extra utility buttons
extramenu = [["A", "End Order"], ["R", "Report of Sales"]]
# Var hamount - lamount: counts how many of each item was ordered
hamount = 0
camount = 0
famount = 0
oamount = 0
samount = 0
lamount = 0
# Var Selection: the current selection to be added to the order
selection = ""
# Var newcustomer: basically, do you want a new customer
newcustomer = True


# Clears console, prints welcome message, waits (waitime) amount of seconds, clears console
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to the final project.")
time.sleep(waitime)
os.system('cls' if os.name == 'nt' else 'clear')

# Menu system
while newcustomer == True:
    while valid == False:
        # Prints Main Menu
        for entry in menu:
            a, b, c = entry
            print("{:<8}{:<20}${:<10.2f}".format(a, b, c))
        # Lazy New Line
        print("")
        # Prints Utility Menu
        for entry in extramenu:
            a, b = entry
            print("{:<8}{:<20}".format(a, b))
        selection = input("What is your selection? ")
        if selection.lower() == "h": 
            valid = False
            hamount += 1
        elif selection.lower() == "c":
            valid = False
            camount += 1
        elif selection.lower() == "f":
            valid = False
            famount += 1
        elif selection.lower() == "o":
            valid = False
            oamount += 1
        elif selection.lower() == "s":
            valid = False
            samount += 1
        elif selection.lower() == "l":
            valid = False
            lamount += 1
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Not a Valid Selection")
            print("Please Try Again")
            print("")