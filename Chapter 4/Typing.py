# Kyle Wenzel
# November 19th, 2020
# Typing Program

print("Welcome to the Typing program. ")

dwarves = ("Doc", "Happy", "Sneezy", "Sleepy", "Bashful", "Grumpy", "Dopey")

for dwarf in dwarves: 
    wpm = input("How many words can", dwarf, "type? ")
    if wpm > 25: 
        print(dwarf + ", you are typing fast enough to pass keyboarding. ")
    elif wpm <= 25: 
        print("Sorry, " + dwarf + ", you are not fast enough to pass keyboarding. ")
    else: 
        print("You have broken yourself. ")