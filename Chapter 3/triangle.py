# Kyle Wenzel
# October 6th, 2020
# triangle Program
# This program will 
# Variable list: 
#   var1 - description
#   var2 - description

print("Welcome to the triangle Program\n")

side1 = int(input("What is the length first side of the triangle? "))
side2 = int(input("What is the length second side of the triangle? "))
side3 = int(input("What is the length third side of the triangle? "))

if side1 == side2 and side1 == side3 and side2 == side3:
    triangle = "Equilateral"
elif side1 != side2 and side1 != side3 and side2 != side3:
    triangle = "Scalene"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle = "Isosceles"
else:
    print("Stop messing around with my program. ")
    print("I don't even know how you got here. ")
    exit()

print("\nThe triangle you input was a", triangle, "triangle")

# Step : Wait for escape keystroke
input("\nPress enter to exit...")