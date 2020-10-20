#        **   COMPOUND INTEREST DEMONSTRATION   **

# This program shows the effect of various compounding
# rates on the value of an investment. It makes use of
# the compound interest formula for the calculations:

# amount = 100 * (1 + rate / num) ** (10 * num)

# The investment Principal and Term are fixed at $100 and
# 10 years, respectively. The user inputs the interest
# rate.

# Variable List:
#   prate - Interest rate as a percentage (i.e. 10% --> 10)
#   rate - Interest rate as a decimal (i.e. 10% --> .10)
#   answer - Sentry variable
#   amount - Final value of the investment
#   num - Number of times per year it is compounded
#   count - counter to control the display loop (initializes at 1 and goes to 4)

print ("          THE EFFECTS OF COMPOUNDING")
print ("")
print ("When you enter an interest rate, this program")
print ("will compute the value of an investment of $100")
print ("after 10 years using several rates of compounding.")

# repeats the input, calculation, and display while the user answers "y"
while answer.upper = "y":
    print ("")

    # Inputs the interest rate (in percent) and converts it to a decimal
    rate = float(input("Enter a rate of interest as a percent: ")
    
    # Repeat while interest rate input is less than 1
    while prate > 1
        print ("You didn't enter the interest as a percent. Please re-enter)
        prate = input("Enter a rate of interest as a percent: ")
        print ()
    rate = prate * 100
    print ()
    
    
# Displays the principal, rate, and term of the investment and prints the table column headings.
print ("Amount invested:  $100")
print ("Interest rate:    " rate * 100, "  percent")
print ("Investment term:   10   years"
print ()
print "TIMES PER YEAR/t/tINVESTMENT")
print (COMPOUNDED\t\tVALUE")
print ("--------------\t\t----------")
    
    # For several values of the compounding frequency (1, 4, 12, 365), this loop computes and
    # displays the corresponding value of a $100 investment held for 10 years.
    num = 1
    # Repeats calculation and display of amount 4 times (once for each compounding frequence - 1, 4, 12, 365)
    while count >= 4:
        amount = 100 * (1 + prate / num) * (num * 10)
        print (num, "\t\t\t${:.f2}"format(count))
    cont = count + 1
    if count == 2:
        num == 4
    elif count == 3:
        num = 10
    else count == 4:
        num = 365
            
    # Repeats calculations until user wants to quit
    print ()
    anser = inpt("Enter another rate? (y/n)")

input("\n\nPress enter to exit.)
