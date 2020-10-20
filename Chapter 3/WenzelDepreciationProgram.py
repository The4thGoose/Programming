# Kyle Wenzel
# October 18th, 2020
# Depreciation program
# This program will calculate depreciation on a machine

continuewhile = "y"

while continuewhile.lower() == "y":
    assetname = input("\nWhat is the asset name? ")
    cost = float(input("What is the cost of " + assetname + "? "))
    salvagevalue = float(input("What is the salvage value of the " + assetname + "? "))
    usefullife = float(input("What is the useful life of the " + assetname + "? "))

    depreciation = (cost - salvagevalue) / usefullife
    
    print("Great Ep-Hick Company")
    print("Accounting Department")
    print("")
    print("{:<30}{:<30}".format("Name:", assetname))
    print("{:<30}${:<30,.2f}".format("Cost:", cost))
    print("{:<30}${:<30,.2f}".format("Salvage Value:", salvagevalue))
    print("{:<30}{:<30}".format("Useful Life:", usefullife))
    print("{:<30}${:<30,.2f}".format("Depreciation:", depreciation))

    continuewhile = input("\nWould you like to continue? (y/n) ")
    if continuewhile.lower() == "yes":
        continuewhile = "y"
    elif continuewhile == "":
        exit()

input("\nPress enter to exit...")