# Kyle Wenzel
# October 8th, 2020
# Celestial Weight Program
# This program will create a menu and calculate your weight on diffrent planets

import random

print("\nWelcome to the Celestial Weight Program.")

print("\nPlease select an option:")
print('''\tVenus.....Press 1
\tMoon......Press 2
\tMars......Press 3
\tJupiter...Press 4''')

selection = int(input("Please select an option: "))

if selection == 1:
    planet = "Venus"
    gravfactor = 0.91
elif selection == 2:
    planet = "Moon"
    selection = 0.17
elif selection == 3:
    planet = "Mars"
    selection = 0.38
elif selection == 4:
    planet = "Jupiter"
    selection = 2.54
else:
    num = random.randint(0, 2)
    if num == 1:
        print("\nError code: ID10T")
        print("You broke something. \n")
        exit()
    elif num == 2:
        print("\nError code: PBCAK")
        print("You broke something. \n")
        exit()
    else:
        print("\nWow, you really messed up.")
        print("You managed to break the code to PRINT AN ERROR\n")

originalweight = float(input("What is your earth weight (in lbs)? "))

otherplanetweight = originalweight * selection

print("{:<15}{:<30}".format("\nPlanet", " Planet Weight"))
print("{:<15}{:<30,.2f}".format("Earth", originalweight))
print("{:<15}{:<30,.2f}".format(planet, otherplanetweight))