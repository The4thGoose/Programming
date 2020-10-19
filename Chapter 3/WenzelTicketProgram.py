ticket = 1
cot = 10.75
cpt = 10.75
print("{:<31}{:<30}".format("\nQuantity of Tickets", "Total Cost of Tickets"))
while ticket <= 12:
    print("{:<30}${:<30}".format(ticket, cot))
    ticket += 1
    cot = ticket * cpt

input("\nPress enter to exit...")