# Kyle Wenzel, Patrick Rao
# September 15th, 2020
# Bowling Program
# This program will 
# Variable list: 
#   cardig1 - Score 1 of #
#   cardig2 - description
#   cardig3 - 
#   nickig1 - 
#   nickig2 - 
#   nickig3 - 
#   hayesg1 - 
#   hayesg2 - 
#   hayesg3 - 
#   epsteing1 - 
#   epsteing2 - 
#   epsteing3 - 
#   cardiaverage - 
#   nickiaverage - 
#   hayesaverage - 
#   epsteinaverage - 
#   carditotal - 
#   nickitotal - 
#   hayestotal - 
#   epsteintotal - 
#   celebtotal - 
#   teachertotal - 

print("Welcome to the Bowling Program\n")

# Step 1: Assign Variables to scores
cardig1 = 101
cardig2 = 126
cardig3 = 132
nickig1 = 135
nickig2 = 117
nickig3 = 123
hayesg1 = 199
hayesg2 = 218
hayesg3 = 221
epsteing1 = 220
epsteing2 = 197
epsteing3 = 236

# Step 2: Determine Averages
cardiaverage = (cardig1 + cardig2 + cardig3)/3
nickiaverage = (nickig1 + nickig2 + nickig3)/3
hayesaverage = (hayesg1 + hayesg2 + hayesg3)/3



# Step 3.1: Calcuclate celebrity team total
carditotal = cardig1 + cardig2 + cardig3
nickitotal = nickig1 + nickig2 + nickig3

celebtotal = carditotal + nickitotal

print("The total score for the celebrity team was: ", celebtotal)

# Step : Wait for escape keystroke
input("\nPress enter to exit...")