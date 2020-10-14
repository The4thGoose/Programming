# Kyle Wenzel
# October 5st, 2020
# Hello Program
# This program will 
# Variable list: 
#   var1 - description
#   var2 - description

print("Welcome to the hello Program\n")

# Step 1: 
print('''\tSelect the language: 
         English.....1
         Spanish.....2
         French......3
         Russian.....4''')
selection = int(input("\nSelect an option... "))

if selection == 1:
    lang = "English"
    hello = "Hello"
elif selection == 2:
    lang = "Spanish"
    hello = "Hola"
elif selection == 3:
    lang = "French"
    hello = "Bonjour"
elif selection == 4:
    lang = "Russian"
    hello = "Здравствуйте"
else:
    print("Why can't you follow directions?")
    exit()

print("The way you say hello in", lang, "is", hello)


# Step : Wait for escape keystroke
input("\nPress enter to exit...")