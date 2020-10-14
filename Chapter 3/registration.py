# Kyle Wenzel
# October 5th, 2020
# Registration Program
# This program will 
# Variable list: 
#   var1 - description
#   var2 - description

print("Welcome to the Registration Program\n")

# Step 1: 
print("What is your Grade Level?")
print("freshman: press 9")
print("sophomore: press 10")
print("junior: press 11")
print("senior: press 12")
grade = int(input("\nPress the cooresponding number"))

if grade != 9 or grade != 10 or grade != 11 or grade != 12:
    if grade < 9:
        print("Aren't you a little too young to be a High Schooler?")
        print("\tYes I am.")
        print("OK then. ")
        exit()
    if grade > 12:
        print("Get outta here dinosaur!")
        exit()
elif grade == 9:
    date = "August 11th"
elif grade == 10:
    date = "August 12th"
elif grade == 11:
    date = "August 13th"
elif grade == 12:
    date = "August 14th"
else: 
    print("Invalid, are you sure you're human?")
    exit()

print("The registration date for grade", grade, "is", date)

# Step : Wait for escape keystroke
input("\nPress enter to exit...")