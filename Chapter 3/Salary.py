# Kyle Wenzel
# October 16th, 2020
# Salary Program
# This program will calculate the amount an employee makes. 

print("\nWelcome to the Salary Program\n")

name = input("What is your employee name? ")
hours = float(input("How many hours did " + name + " work? "))

total = hours * 15

print("\nEmployee", name, "earned ${:,.2f}".format(total))

input("\nPress enter to exit")