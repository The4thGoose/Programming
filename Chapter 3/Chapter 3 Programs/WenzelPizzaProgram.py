# Kyle Wenzel
# October 9th, 2020
# Pizza Program
# This program will ask for the amount of pizzas, size and other conditions and calculate the final cost

print("\nWelcome to the Pizza program. ")

print("Please select an option. \n")
print(''' 6 inch ($4).......Press 1
10 inch ($7.50)....Press 2
14 inch (12.90)....Press 3
16 inch ($14.25)...Press 4''')
selection1 = int(input("\nEnter your selection: "))

if selection1 != 1 and selection1 != 2 and selection1 != 3 and selection1 != 4:
    print("\nNot a valid selection.")
    exit()

if selection1 == 1:
    size = 6
    sizecost = 4
    cpt = "$0.50"
    cptm = 0.5
elif selection1 == 2:
    size = 10
    sizecost = 7.5
    cpt = "$0.60"
    cptm = 0.6
elif selection1 == 3:
    size = 14
    sizecost = 12.9
    cpt = "$0.75"
    cptm = 0.75
elif selection1 == 4:
    size = 16
    sizecost = 14.25
    cpt = "$0.90"
    cptm = 0.9

print("\nThe cost per topping for a", size, "inch pizza is", cpt)
selection2 = int(input("Enter the amount of toppings you would like: "))

if selection1 == 1 or selection1 == 2:
    extracheese = 1
elif selection1 == 3 or selection1 == 4:
    extracheese = 2

print("\nThe cost for extra cheese for a", size, "inch pizza is " + "${:.2f}".format(extracheese))
selection3 = input("Would you like extra cheese? (y)es or (n)o: ")
selection3 = selection3.lower()

if selection3 == "y" or selection3 == "yes":
    cheeseselection = 1
elif selection3 == "n" or selection3 == "no":
    cheeseselection = 2
else:
    print("\nYou broke something. ")
    exit()

if cheeseselection == 2:
    extracheese = 0
    endcap = "is: "
elif cheeseselection == 1 and extracheese == 1:
    extracheese = 1
    endcap = "and extra cheese is: "
elif cheeseselection == 1 and extracheese == 2:
    extracheese = 2
    endcap = "and extra cheese is: "
else:
    print("\nHow did you get here? ")
    exit()

pizzasub = sizecost + (cptm * selection2) + extracheese 
pizzatax = pizzasub * 0.06
pizzafinal = pizzasub + pizzatax

print("\nThe final cost for your", size, "inch pizza with", endcap + "${:.2f}".format(pizzafinal))
print("Thank You!")