# Kyle Wenzel
# January 7th, 2021
# GPA Program
import os
import webbrowser
import time
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to the GPA program! ")

freshmancount = 0
sophomorecount = 0
juniorcount = 0
seniorcount = 0
gpaaverage = 0
gpatotal = 0
gpaticker = 0
ahigh = ""
bhigh = ""
ehigh = 0
alow = ""
blow = ""
elow = 100

students = [["White", "Snow", 9, "F", 3.56],
            ["Sprat", "Jack", 12, "M", 2.0],
            ["Contrary", "Mary", 9, "F", 3.674],
            ["Dumpty", "Humpty", 11, "M", 2.342],
            ["Bunny", "Easter", 10, "M", 4.233],
            ["Wonderland", "Alice", 10, "F", 3.755],
            ["Bunyon", "Paul", 11, "M", 1.434],
            ["Penny", "Henny", 9, "F", 2.54],
            ["Hatter", "Mad", 11, "M", 4.522],
            ["Munk", "Chip", 10, "M", 3.0],
            ["Hood", "Red Riding", 10, "F", 3.137],
            ["Bunny", "Bugs", 11, "M", 2.12],
            ["Duck", "Daffy", 11, "M", 3.564],
            ["Ant", "Atom", 12, "M", 3.333],
            ["Mouse", "Mickey", 10, "M", 3.975],
            ["Brown", "Charlie", 9, "M", 1.25]]
sophomores = []
print("{:^30}".format("GPA Menu"))
print("{:<5}{:<10}".format("\n1.", "School List"))
print("{:<5}{:<10}".format("2.", "Sophomores"))
print("{:<5}{:<10}".format("3.", "Juniors"))
print("{:<5}{:<10}".format("4.", "Above Average Students"))
print("{:<5}{:<10}".format("5.", "Alphabetical List"))
print("{:<5}{:<10}".format("6.", "Highest and Lowest GPA"))
print("{:<5}{:<10}".format("7.", "Find Student"))
print("{:<5}{:<10}".format("8.", "Exit"))
print("\nPlease enter an option from the menu:")

selection = int(input("\nPlease enter your selection. "))

if selection == 1:
    # School List
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You have selected: School List")
    ynselection1 = input("Is this correct (y/n)? ")
    if ynselection1.lower() == "y" or ynselection1.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif ynselection1.lower() == "n" or ynselection1.lower() == "no":
        print("Don't worry, we all make mistakes")
        print("Please restart the program after it exits")
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You broke something")
        print("No need to be upset, You can just try again")
        webbrowser.open("https://youtu.be/eY52Zsg-KVI")
        exit()
    print("\nAll Students")
    print("-"*90)
    for entry in students:
        a, b, c, d, e = entry
        print("{:<30}{:<30}{:<30}".format(b, a, c))
        if c == 9:
            freshmancount += 1
        elif c == 10:
            sophomorecount += 1
        elif c == 11:
            juniorcount += 1
        elif c == 12:
            seniorcount += 1
    print("")
    print("Freshman:", freshmancount)
    print("Sophomores:", sophomorecount)
    print("Juniors:", juniorcount)
    print("Seniors:", seniorcount)
elif selection == 2:
    # Sophomores
    print("You have selected: Sophomores")
    ynselection1 = input("Is this correct (y/n)? ")
    if ynselection1.lower() == "y" or ynselection1.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif ynselection1.lower() == "n" or ynselection1.lower() == "no":
        print("Don't worry, we all make mistakes")
        print("Please restart the program after it exits")
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You broke something")
        print("No need to be upset, You can just try again")
        exit()
        webbrowser.open("https://youtu.be/eY52Zsg-KVI")
    print("Sophomores")
    print("-"*15)
    for entry in students:
        a, b, c, d, e = entry
        if c == 10:
            print(b, a)
elif selection == 3:
    # Juniors
    print("You have selected: Juniors")
    ynselection1 = input("Is this correct (y/n)? ")
    if ynselection1.lower() == "y" or ynselection1.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif ynselection1.lower() == "n" or ynselection1.lower() == "no":
        print("Don't worry, we all make mistakes")
        print("Please restart the program after it exits")
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You broke something")
        print("No need to be upset, You can just try again")
        exit()
        webbrowser.open("https://youtu.be/eY52Zsg-KVI")
    print("Juniors")
    print("-"*15)
    for entry in students:
        a, b, c, d, e = entry
        if c == 11:
            print(b, a)
elif selection == 4:
    # Above Average Students
    print("You have selected: Above Average Students")
    for entry in students:
        a, b, c, d, e = entry
        gpaticker += 1
        gpatotal += e
    gpaaverage = gpatotal / gpaticker
    print("{:<30}{:<30}{:<30}".format("First Name", "Last Name", "GPA"))
    print("-"*90)
    for entry in students:
        a, b, c, d, e = entry
        if e > gpaaverage:
            print("{:<30}{:<30}{:<30}".format(b, a, e))
elif selection == 5:
    # Alphabetical List
    print("You have selected: Alphabetical List")
    print("I spent almost 2 hours trying to figure this one out,")
    print("I couldn't figure it out")
    print("So instead, I present to you: My favorite video on the internet")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Now playing: Impractical Engineering by Uncle Dane")
    webbrowser.open("https://youtu.be/YgtSWCt5MgU")
elif selection == 6:
    # Highest and Lowest GPA
    print("You have selected: Highest and Lowest GPA")
    ynselection1 = input("Is this correct (y/n)? ")
    if ynselection1.lower() == "y" or ynselection1.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif ynselection1.lower() == "n" or ynselection1.lower() == "no":
        print("Don't worry, we all make mistakes")
        print("Please restart the program after it exits")
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You broke something")
        print("No need to be upset, You can just try again")
        exit()
        webbrowser.open("https://youtu.be/eY52Zsg-KVI")
    for entry in students:
        a, b, c, d, e = entry
        if ehigh < e:
            ehigh = e
            ahigh = a
            bhigh = b
        if elow > e:
            elow = e
            alow = a
            blow = b
    print("The student with the highest GPA is", bhigh, ahigh)
    print("The student with the lowest GPA", blow, alow)
elif selection == 7:
    # Find Student
    print("You have selected: Find Student")
    ynselection1 = input("Is this correct (y/n)? ")
    if ynselection1.lower() == "y" or ynselection1.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif ynselection1.lower() == "n" or ynselection1.lower() == "no":
        print("Don't worry, we all make mistakes")
        print("Please restart the program after it exits")
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You broke something")
        print("No need to be upset, You can just try again")
        exit()
        webbrowser.open("https://youtu.be/eY52Zsg-KVI")
    searchterma = input("Please enter the last name of the student you want to search for. ")
    for entry in students:
        a, b, c, d, e = entry
        if searchterma.lower() == a.lower():
            fullname = b, a
            print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(b, a, c, d, e))
elif selection == 8:
    # Exit
    print("You have selected: Exit")
    print("Goodbye")
    os.system('cls' if os.name == 'nt' else 'clear')
else:
    # Error
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You broke something")
    print("No need to be upset, You can just try again")
    webbrowser.open("https://youtu.be/eY52Zsg-KVI")

input("\nPress enter to exit...")
os.system('cls' if os.name == 'nt' else 'clear')