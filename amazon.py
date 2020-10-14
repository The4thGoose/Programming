price = float(input("What is the cost of the item: "))
percent = float(input("Enter percent off in decimal format: "))
saved = price * percent
final = price - saved
print("The final price is: ", {:.2f}.format(final))