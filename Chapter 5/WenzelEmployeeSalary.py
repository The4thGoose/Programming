# Kyle Wenzel
# December 10th, 2020
# Employee Salary Program

print("Welcome to the ProgramName Program\n")

# Step 1: 
employeelist = []
salarylist = []
ticker = 0
totalsalary = 0
above = 0
atav = 0
below = 0
anotheremployee = "y"
while anotheremployee == "y":
    employee = input("What is the employee's name? ")
    employeelist.append(employee)
    ansalary = float(input("What is the annual salary for this employee? "))
    salarylist.append(ansalary)
    ticker += 1
    anotheremployee = input("Whould you like to enter another employee? (y or n) ")
for entry in salarylist:
    totalsalary += entry
averagesalary = totalsalary / ticker
for entry in salarylist: 
    if entry < averagesalary:
        below += 1
    elif entry == averagesalary: 
        atav += 1
    elif entry > averagesalary: 
        above += 1
print("{:}${:,.2f}".format("Total Employee Salary:", totalsalary))
print("{:}${:,.2f}".format("Average Employee Salary:", averagesalary))

print("{:}{:,}".format("Number of Employees Making More than the Average:", above))
print("{:}{:,}".format("Number of Employees Making the Average:", atav))
print("{:}{:,}".format("Number of Employees Making Less than the Average:", below))
# Step : Wait for escape keystroke
input("\nPress enter to exit...")