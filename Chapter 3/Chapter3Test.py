# Kyle Wenzel
# October 29th, 2020
# Chapter 3 Test Program
# Variable List:
#   name - the name of the user
#   totalsubscriptions - the total number of subscriptions
#   subscriptions - the number of subscriptions sold by a user
#   num - the number of the error code

# Used to randomly choose an error code
import random

print("\tWelcome to the chapter 3 Test program!\n")

# Define variables for total subscriptions and the first name
totalsubscriptions = 0
name = "open"

# SOOOOURCE SPAGHETIIIIIII (SPOOPY)
while name:
    # Ask For Name
    name = input("\nWhat is your name? ")
    # If the name is not empty, continue with the program
    if name: 
        # Ask for subscriptions sold
        subscriptions = int(input("How many subscriptions did you sell? "))
        # Print the reward
        if subscriptions >= 40:
            print("\nYour award is a $50 gift certificate and an award plaque. ")
        elif subscriptions >= 20:
            print("Your award is an award plaque. ")
        elif subscriptions < 20 and subscriptions > 0:
            print("Your award is a certificate. ")
        else:
            # Generate a number for the error code and print it
            num = random.randint(0, 2)
            if num == 1:
                print("\nError code: ID10T")
                print("You broke something. \n")
                print("Please Google error code for help. \n")
                exit()
            elif num == 2:
                print("\nError code: PBCAK")
                print("You broke something. \n")
                print("Please Google error code for help. \n")
                exit()
            else:
                print("\nWow, you really messed up.")
                print("You managed to break the code to PRINT AN ERROR\n")
        # Add subscriptions to totalsubscriptions
        totalsubscriptions = totalsubscriptions + subscriptions

# Print final message
print("\nYour total members' sales are", totalsubscriptions, "subscriptions.")
print("Thank you!")

input("\nPress enter to exit...")