# Kyle Wenzel
# November 12th, 2020
# Miles Per Gallon Program
# THis program will

print("Welcome to the Miles per Gallon Program. ")

week = 1
totalgallons = 0
for i in range(4):
    print("\n\tWeek", week)
    gallonsthisweek = float(input("How many gallons of gas did you use this week? "))
    milesthisweek = float(input("How many miles did you drive this week? "))
    mpgthisweek = float(milesthisweek / gallonsthisweek)
    print("{:}{:}{:}{:,.2f}".format("\nThe mpg for week", week, "is", mpgthisweek))
    week += 1