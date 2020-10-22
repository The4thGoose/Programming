# Kyle Wenzel
# October 14th, 2020
# PBS Pledge Program
# This program will ask for donator's name, how much they pledged, how many people pledged, how much was made, and the average pledge

print("\nWelcome to the PBS Pledge Program! ")
donators  = 0
donatedtotal = 0
name = input("What is the donator's name (Press enter when finished)? ")
if name != "":
    donated = float(input("How much did they pledge (Press enter when finished)? "))

while name != "":
    name = name.title()
    if donated > 500:
        rank = "You are a PLATINUM DONATOR! "
    elif donated >= 100 and donated < 500:
        rank = "You are a GOLD DONATOR! "
    elif donated >= 50 and donated < 100:
        rank = "You are a SILVER DONATOR! "
    elif donated < 50:
        rank = "Thank you for your donation. "
    else:
        print("ERROR CODE: PBCAK")
        exit()
    print("Thanks", name, "-", rank)
    donators += 1
    donatedtotal = donatedtotal + donated
    name = input("What is the donator's name (Press enter when finished)? ")
    if name != "":
        donated = float(input("How much did they pledge (Press enter when finished)? "))

averagedonation = donatedtotal / donators

print("PBS Pledge Summary Report\n")

print("{:<30}{:<30,}".format("Total # of Donators:", donators))
print("{:<30}${:<30,.2f}".format("Total Pledges:", donatedtotal))
print("{:<30}${:<30,.2f}".format("Average Pledge:", averagedonation))