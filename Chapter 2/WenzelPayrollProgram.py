# Kyle Wenzel
# September 24th, 2020
# Payroll Program
# This program will calculate and print payrolls for the Great Epstein company
# Variable list: 
#   var1 - description
#   var2 - description

print("Welcome to the Payroll Program\n")

# Step 1: 
name  = input("What is your first and last name? ")
namet = name.title()

if namet == "Lucas Johnson":
    easy = 1
elif namet == "Jalen Chan":
    easy = 2
elif namet == "Sofie Demare":
    easy = 3
elif namet == "Sofie DeMare":
    easy = 3
elif namet == "Sniya Gorthi":
    easy = 4
else:
    print("Not a name in the pay database. ")
    input("\nPress enter to exit...")
    exit()

if easy == 1:
    payrate = 8.35
elif easy == 2:
    payrate = 15.5
elif easy == 3:
    payrate = 13.25
elif easy == 4:
    payrate = 13.5

hours = float(input("\nHow many hours have you worked this week? "))

if hours > 168:
    print("\nNot possible, stop lying.\n")
    exit()
elif hours == 0: 
    print("I don't know about that one chief...")
    exit()
elif hours < 0:
    print("What are you, Marty McFly?")
    exit()

gpay = payrate * hours
sstax = gpay * 0.07
fedtax = gpay * 0.15
netpay = gpay - (sstax + fedtax)

print("{:<15}{:>20}".format("\nName: ", namet))
print("{:<15}{:>19.2f}".format("Pay Rate: ", payrate))
print("{:<15}{:>19.2f}".format("Hours Worked: ", hours))
print("{:<15}{:>19.2f}".format("Gross Pay: ", gpay))

print("\nDeductions")
print("{:<15}{:>10.2f}".format("\tSocial Security:", sstax))
print("{:<15}{:>12.2f}".format("\tFederal Tax:", fedtax))

print("{:<15}{:>19.2f}".format("Net Pay:", netpay))

# Step : Wait for escape keystroke
input("\nPress enter to exit...")