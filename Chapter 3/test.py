print("Select a six flags location:")
print('''\n        Los Angeles,  California...Press 1
        Chicago, Illinois..........Press 2
        Louisville, Kentucky.......Press 3
        New Orleans, Louisiana.....Press 4
        St. Louis, Missouri........Press 5''')
selection = input("\n\nEnter your selection: ")

lacost = 60
chicagocost = 70
louisvillecost = 45
neworleanscost = 50
stlouiscost = 60

if selection == 1:
    location = "Los Angeles, California"
    cost = lacost
elif selection == 2:
    location = "Chicago, Illinois"
    cost = chicagocost
elif selection == 3:
    location = "Louisville, Kentucky"
    cost = louisvillecost
elif selection == 3:
    location = "New Orleans, Louisiana"
    cost = neworleanscost
elif selection == 4:
    location = "St. Louis, Missouri"
    cost = stlouiscost

print("The cost for a ticket in", location, "is", cost, "dollars")