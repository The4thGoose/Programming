##Name: Kyle Wenzel
##Date: 9/8/2020
##Program Name: Birthday List.py
##Program Description: Prints a birthday list with prices

##Step 1: Print Headers
print("{:<15}{:<70}{:>15}{:>15}".format("Quantity", "Item Name/ Description", "Price", "Total"))

##Step 2: Print Items in List
print("{:<15}{:<70}{:>16}{:>15}".format("\n1", " Power Adapter DR-E5 DC Coupler Charger Kit for Canon EOS Rebel T1i", 13.99, 13.99))
print("{:<15}{:<70}{:>15}{:>15}".format("1", "AMD Ryzen 5 3600X", 249.99, 249.99))
print("{:<15}{:<70}{:>11,.2f}{:>15,.2f}".format("2", "NVIDIA Titan Xp Star Wars Galactic Empire Collectors Edition Graphics Card", 2179.00, 4358.00))

##Step 3: Wait for exit keystroke
input("\nPress enter to exit...")