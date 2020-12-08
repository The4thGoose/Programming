# Kyle Wenzel
# December 8th, 2020
# Game Program

print("Welcome to the Games program. ")

import os
os.system('cls' if os.name == 'nt' else 'clear')

counter = 1

print ("Welcome to the Candy Program")
#Step 1:______
game = []
numberlist = 1
for item in range (1,6):
    FGAME = input("What is game #" + str(numberlist) + "? ")
    numberlist += 1
    game.append(FGAME)

game.sort()
for item in game: 
    print(item)