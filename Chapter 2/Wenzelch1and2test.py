# Kyle Wenzel
# MonthDay, 2020
# Chapter 1 and 2 test Program
# This program will get the names of 3 movies and tickets sold and calculate total sales
# Variable list: 
#   movie1 - name of movie 1
#   movie2 - name of movie 2
#   movie3 - name of movie 3
#   tickets1 - how many tickets where sold for movie 1
#   tickets2 - how many tickets where sold for movie 2
#   tickets3 - how many tickets where sold for movie 3
#   cpt - cost per ticket
#   total1 - total sales for movie 1
#   total2 - total sales for movie 2
#   total3 - total sales for movie 3

print("Welcome to the Chapter 1 and 2 test Program\n")

# Step 1: ask for name of 3 movies
movie1 = input("What is the name of the first movie? ")
movie2 = input("What is the name of the second movie? ")
movie3 = input("What is the name of the third movie? ")

# Step 2: ask how many tickets where sold for all movies
tickets1 = float(input("How many tickets were sold for " + movie1 + "? "))
tickets2 = float(input("How many tickets were sold for " + movie2 + "? "))
tickets3 = float(input("How many tickets were sold for " + movie3 + "? "))

# Step 3: define cost of ticket and calculate total sales
cpt = 7
total1 = tickets1 * cpt
total2 = tickets2 * cpt
total3 = tickets3 * cpt

# Step 4: print the movie titles, tickets sold, and total sales in a nice chart
print("{:<30}{:<15}{:<15}".format("Movie Title", "Tickets Sold", "Total Sales"))
print("{:<30}{:<15,.0f}${:<15,.2f}".format(movie1, tickets1, total1))
print("{:<30}{:<15,.0f}${:<15,.2f}".format(movie2, tickets2, total2))
print("{:<30}{:<15,.0f}${:<15,.2f}".format(movie3, tickets3, total3))
print("\nThese numbers were calculated with a cost per ticket of ", cpt)

# Step : Wait for escape keystroke
input("\nPress enter to exit...")