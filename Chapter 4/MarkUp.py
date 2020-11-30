# Kyle Wenzel
# November 23rd, 2020
# Mark Up program

print("Welcome to the Mark Up Program")
print("")
count = 0
items = ("Teddy Bear", "Toy Train", "Hoola Hoop", "Betsy Wetsy", "Pogo Stick")
wcost = (12.5, 58.75, 10, 15, 11)
markup = (5, 23.5, 4, 6, 4.4)
retailcost = (17.5, 52.25, 14, 21, 15.4)

print("{:<20}{:<10}{:<10}{:<10}".format("Item", "Cost", "Mark Up", "Retail"))
print("")

for item in items:
    print("{:<20}{:<10,.2f}{:<10,.2f}{:<10,.2f}".format(item, wcost[count], markup[count], retailcost[count]))
    count += 1

input("\nPress enter to exit...")