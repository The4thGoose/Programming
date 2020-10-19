# Kyle Wenzel
# October 18th, 2020
# Depreciation program
# This program will calculate depreciation on a machine


assetname = input("\nWhat is the asset name? ")
cost = float(input("What is the cost of", assetname + "? "))
salvagevalue = float(input("What is the salvage value of the", assetname + "? "))
usefullife = float(input("What is the useful life of the", assetname + "? "))

depreciation = (cost - salvagevalue) / usefullife

print("Great Ep-Hick Company")
print("Accounting Department")
print("")
print("{:<30}{:<30}".format())
print("{:<30}{:<30}".format())
print("{:<30}{:<30}".format())
print("{:<30}{:<30}".format())
print("{:<30}{:<30}".format())