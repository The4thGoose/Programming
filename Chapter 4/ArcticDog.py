# Kyle Wenzel
# November 30th, 2020
# Arctic Dog Program

print("Welcome to the Arctic Dog program. ")
count = 0
total = 0

sales = (28, 30, 24, 10, 12, 10, 5, 3, 4, 10, 21, 25)
months = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print("")
print("{:<25}{:<40}".format("Month", "\tSales"))

for sale in sales: 
    bar = "*" * sale
    print("{:<25}{:<40}".format(months[count], bar))
    total += sale
    count += 1
print("{:<25}{:<40}".format("Total sold for 2020", total))

input("\nPress enter to exit...")