# The Happy Health Club has updated its requirements for membership. 
# New members must be between the age of 21 and 55, 
# with an income of no less than $50,000 a year. 
# Write a condition that expresses these conditions.

age = float(input("How old are you? "))
income = float(input("How much money did you make this year? "))

if age >= 21 and age < 55:
    if income >= 50000:
        print("True")
    else:
        print("False")
        input("Press enter to exit...")
        exit()
else:
    print("False")
    input("Press enter to exit...")
    exit()