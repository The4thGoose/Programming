# Kyle Wenzel
# December 1st, 2020
# Chapter 4 Test Program
# Variable List: 
#   championshiplist: list of championships
#   championshipcostlist: average ticket price for championships
#   count: counter
#   championship: assignee for championshiplist
#   totalcost: totalcost for all championships (accumulator)

# Step 0: Clear terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Step 1: Welcome Message
print("\nWelcome to the Chapter 4 Test Program. ")

# Step 2: initalize Variables
championshiplist = ("Cubs 2016 World Series", "Blackhawks 2015 Stanley Cup", "White Sox 2005 World Series", "Bulls 1998 NBA Championship", "Bears 1985 Super Bowl")
championshipcostlist = (4700, 2200, 1200, 45, 60)
count = 0
totalcost = 0

# Step 3: Print header for list
print("{:<41}{:<30}".format("\nChicago Championships", "Average Ticket Price"))

# Step 4: Create Loop for all items in list
for championship in championshiplist: 
    # Step 4.1: Print Meat of Body
    print("{:<40}${:<30,.2f}".format(championshiplist[count], championshipcostlist[count]))
    # Step 4.2: Add to total cost
    totalcost += championshipcostlist[count]
    # Step 4.3: Tick counter up by 1
    count += 1

# Step 5: Print total for all games
print("{:<41}${:<30,.2f}".format("\nTotal Cost to Attend All Games", totalcost))

printcount = count - 1
selection = int(input("\nPlease choose a number between 0 and " + str(printcount) + ": "))
if selection < 0 or selection > printcount:
    print("Not a valid selection. ")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()
print("You have won sports memorabilia from the", championshiplist[selection])

input("\nPress enter to exit...")
print("")