# This program calculates the area of a rectangular room for ordering flooring.

print("Enter length of room measured in feet")
length = float(input())
print("Enter width of room measured in feet")
width = float(input())
square_yards = (length) * (width) / 9

print("You need to order " + str(square_yards) + " square yards of flooring.")
