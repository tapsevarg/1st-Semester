# This is a program to calculate the area of a rectangular room when ordering flooring.
2	
3	print ("Enter length of room measured in feet")
4	length = float(input())
5	print ("Enter width of room measured in feet")
6	width = float(input())
7	
8	square_yards = (length)*(width)/9
9	
10	print ("You need to order " + str(square_yards) + " square yards of flooring.")