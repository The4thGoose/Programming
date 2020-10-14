# Kyle Wenzel
# October 5th, 2020
# Video Game Program
# This program will 
# Variable list: 
#   var1 - description
#   var2 - description

print("Welcome to the Video Game Program\n")

# Step 1: 
score = float(input("What is your score?"))

if score >= 50000:
    points = "You completed the highest level!"
elif score >= 35000 and score < 50000:
    points = "You completed level 2"
elif score >= 20000 and score < 35000:
    points = "You completed level 1"
elif score < 20000:
    points = "You didn't achieve a rating. "

print("Due to your score of", score)
print(points)

# Step : Wait for escape keystroke
input("\nPress enter to exit...")