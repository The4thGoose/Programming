# Kyle Wenzel
# December 14th, 2020

print("Welcome to the DMV Program. ")

criminal = [("Tommy Porter", "P12345", 11),
            ("Sarayu Suresh", "S67890", 8),
            ("Elaina Littig", "L45678", 2),
            ("Sniya Gorthi", "G23456", 10),
            ("Andy Webb", "W90123", 5),
            ("Nick Erazo", "E78901", 15),
            ("Katherine Columbus", "C34567", 7),
            ("Lakshyaa Nathan", "N56789", 4)]



criminal.sort()
for entry in criminal:
    a, b, c=entry
    print (a)


AFIS = input("\nWhat is the license number? ")
print("")
found = 0
for entry in criminal:
    a, b, c = entry
    if AFIS.lower() == b.lower():
        print("\nNaperville Trouble Maker:", a)
        print("\nOutstanding Warrants:", c)
        print ("\n\tPULL THIS PERSON OVER IMMEDIATELY AND ARREST THEM!")
        found = 1
if found == 0:
    print("they are free to go")

input ("\nPress enter to exit")




input("Press enter to exit...")