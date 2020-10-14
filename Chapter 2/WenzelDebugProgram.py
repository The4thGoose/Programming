#       ***   Swimming Pool Calculations   ***
#              Chapter 2 Debug Program
#
#   This program inputs the diameter of a pool and the
#   per-foot-cost of the pool and decking, and prints the
#   area and circumference of the pool, and the total cost
#   of the pool and its decking.
#
#   Variable List:
#      area ............ area of pool
#      circumference ... circumference of pool
#      customer ....... name of customer
#      deckcost ........ total cost of decking
#      deckftcost ...... cost per foot of decking ($10)
#      diameter ........ diameter of pool
#      poolcost ........ total cost of pool
#      poolftcost ...... cost per square foot of pool ($20)
#      radius .......... radius of pool


print("Welcome to Rosebud Swimming Pools")
print("")
print("Area, Circumference and Decking Cost Calculator")
print("")
print("")

#   input data
customer = input("Enter the name of the customer: ")
diameter = float(input("Enter the diameter (in feet) of the pool: "))
poolftcost = 10
deckftcost = 20

#   calculation of area, circumference, and decking cost
radius = diameter / 2
area = 3.14 * radius * 2
poolcost = poolftcost * area
circumference = 2 * 3.14 * radius
deckcost = deckftcost * circumference

#   round area and circumference to nearest tenth
area = round(area, 1)
circumference = round(circumference, 1)

#   output results
print
print
print ("Customer:\t\t\t", customer)
print ()
print ("Pool Diameter:\t\t", diameter, "ft.")
print ("Pool Area:\t\t\t", area, "sq. ft.")
print ("Pool Circumference:\t", circumference, "ft.")
print
print ("{:}${:.2f}".format("Cost of Decking = ", deckcost))
print ("{:}${:.2f}{:}".format("    (at ", deckftcost, " per foot)"))
print ("{:}${:.2f}".format("Cost of Pool = ", poolcost))
print ("{:}${:.2f}{:}".format("    (at ", poolftcost, " per square foot)")) 

input("\nPress enter to exit.")