amount = 1
day = 1
while day <= 30:
    print(amount, "pennies")
    if day == 15 or day == 30:
        print("Day", day)
    amount *= 2
    day += 1

input("\nPress enter to exit...")