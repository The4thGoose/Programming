# Kyle Wenzel
# October 22nd, 2020
# Fizz Buzz Program
# This program will 
number = 1

while number < 16:
    if number == 15:
        print("FizzBuzz")
    elif number == 3 or number == 6 or number == 9 or number == 12: 
        print("Fizz")
    elif number == 5 or number == 10:
        print("Buzz")
    else:
        print(number)
    number += 1

input("\nPress enter to exit...")