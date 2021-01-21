# Kyle Wenzel
# January 14th, 2021
# Final Project
# It's a cash register or something, IDK
# You will find the variable dictionary entries right above the respective variable's definition 

# Imports modules
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
# Var htotalamount - ltotalamount: used for calculating sales report
htotalamount = 0
ctotalamount = 0
ftotalamount = 0
ototalamount = 0
stotalamount = 0
ltotalamount = 0
# Var Selection: the current selection to be added to the order
selection = ""
# Var newcustomer: basically, do you want a new customer
newcustomer = True
# Var customervalid: valid selection for new customer question
customervalid = False
# Var d: used in post-order totals to calculate final costs, replaces hamount through lamount in certain circumstances
# Var printprice: used as a buffer to store temporary prices to be printed in menus
printprice = 0
# Var orderprice: used for calculating and determining final price and tax
orderprice = 0
# Var tax: It's... tax
tax = 0
# Var finalorderprice: its the orderprice (subtotal) plus tax
# Var amountcollected: amount of money collected from the customer
amountcollected = 0
# Var changeamount: how much change is owed to the customer
changeamount = 0

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
        # Lazy New Line
        print("")
        # Asks for selection
        selection = input("What is your selection? ")
        # Based on selection, adds one to the ticker for the menu item
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
        elif selection.lower() == "a":
            valid = True
        elif selection.lower() == "r":
            # DON'T FORGET TO IMPLIMENT SALES REPORT
            valid = False
            os.system('cls' if os.name == 'nt' else 'clear')
            for entryitem in menu:
                a, b, c = entryitem
                if a.lower() == "h":
                    # Hamburger
                    # 1.29
                    d = htotalamount * c
                    print("{:<20}${:<20,.2f}${:<10,.2f}".format(b, c, d))
                elif a.lower() == "c":
                    # Cheeseburger
                    # 1.49
                    d = ctotalamount * c
                    print("{:<20}${:<20,.2f}${:<10,.2f}".format(b, c, d))
                elif a.lower() == "f":
                    # Fries
                    # 0.99
                    d = ftotalamount * c
                    print("{:<20}${:<20,.2f}${:<10,.2f}".format(b, c, d))
                elif a.lower() == "o":
                    # Onion Rings
                    # 1.09
                    d = ototalamount * c
                    print("{:<20}${:<20,.2f}${:<10,.2f}".format(b, c, d))
                elif a.lower() == "s":
                    # Small Soft Drink
                    # 0.79
                    d = stotalamount * c
                    print("{:<20}${:<20,.2f}${:<10,.2f}".format(b, c, d))
                elif a.lower() == "l":
                    # Large Soft Drink
                    #1.19
                    d = ltotalamount * c
                    print("{:<20}${:<20,.2f}${:<10,.2f}".format(b, c, d))
            input("Press enter to continue...")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Not a Valid Selection")
            print("Please Try Again")
            print("")
        customervalid = False
        os.system('cls' if os.name == 'nt' else 'clear')
    # Sales Report
    print("{:<20}{:<20}{:<10}".format("Item", "Quantity", "Sales"))
    for entry in menu:
        a, b, c = entry
        if a.lower() == "h":
            d = hamount
            htotalamount += hamount
        elif a.lower() == "c":
            d = camount
            ctotalamount += camount
        elif a.lower() == "f":
            d = famount
            ftotalamount += famount
        elif a.lower() == "o":
            d = oamount
            ototalamount += oamount
        elif a.lower() == "s":
            d = samount
            stotalamount += samount
        elif a.lower() == "l":
            d = lamount
            ltotalamount += lamount
        printprice = float(d * c)
        orderprice += printprice
        print("{:<20}{:<20}${:<10,.2f}".format(b, d, printprice))
    # Ask for input (press enter to continue)
    input("Press enter to continue...")
    # Clear Console
    os.system('cls' if os.name == 'nt' else 'clear')
    # Calculate tax and print menus
    tax = orderprice * 0.05
    finalorderprice = orderprice + tax
    print("{:<10}${:<10,.2f}".format("Subtotal:", orderprice))
    print("{:<10}${:<10,.2f}".format("Tax:", tax))
    print("{:<10}${:<10,.2f}".format("Total:", finalorderprice))
    # Ask amount collected
    amountcollected = float(input("\nEnter the amount collected: $"))
    changeamount = amountcollected - finalorderprice
    print("{:<20}${:<20,.2f}".format("Change:", changeamount))
    # Reset hamount through lamount 
    hamount = 0
    camount = 0
    famount = 0
    oamount = 0
    samount = 0
    lamount = 0
    # Asks if you want a new customer
    while customervalid == False:
        customerselection = input("Would you like to enter a new customer (yes/no)? ")
        if customerselection.lower() == "yes" or customerselection.lower() == "y":
            newcustomer = True
            customervalid = True
            valid = False
        elif customerselection.lower() == "no" or customerselection.lower() == "n":
            newcustomer = False
            customervalid = True
            valid = True
        else: 
            customervalid = False
