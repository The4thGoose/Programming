# Kyle Wenzel
# October 7th, 2020
# Income Tax Program
# This program will ask you for your yearly income and calculate how much taxes are due

print("\nWelcome to the Income Tax program")

income = float(input("\nHow much money did you make in the last year? "))

if income > 0 and income <= 8925:
    taxp = 0.1
    taxa = 0
elif income > 8925 and income <= 36250:
    taxp = 0.15
    taxa = 892.5
elif income > 36250 and income <= 87850:
    taxp = 0.25
    taxa = 4991.25
elif income > 87850 and income <= 183250:
    taxp = 0.28
    taxa = 17891.25
elif income > 183250 and income <= 298350:
    taxp = 0.33
    taxa = 44603.25
elif income > 298350 and income <= 400000:
    taxp = 0.35
    taxa = 115586.25
elif income > 400000:
    taxp = 0.396
    taxa = 151163.75
else:
    print("How did you get here?")
    exit()

taxowed = income + ((taxp * income) + taxa)

print("\nBased on your annual income of ${:,.2f}".format(income), "you owe the IRS ${:,.2f}".format(taxowed))
print("Please make your checks payable to Mrs. Epstein.")

input("\nPress enter to exit...")