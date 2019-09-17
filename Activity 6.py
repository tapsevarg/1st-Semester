def calculateArea(length, width, height):
    area = 2 * length * height + 2 * width * height
    
    return area

def calculateCost(paint, price):
    cost = paint * price
    
    return cost

def calculatePaint(area, coverage):
    paint = area / coverage + 0.9999
    
    return paint

def displayResults(cost, paint):
    print("You need " + str(paint) + " gallon(s) of paint, which will cost $" + str(cost) + ".")

def getPaintCoverage():
    print("Enter number of square feet that a gallon of paint will cover")
    coverage = float(input())
    
    return coverage

def getPrice():
    print("Enter price of the paint")
    price = float(input())
    
    return price

def getRoomHeight():
    print("Enter the height of the room")
    height = float(input())
    
    return height

def getRoomLength():
    print("Enter the length of the room")
    length = float(input())
    
    return length

def getRoomWidth():
    print("Enter the width of the room")
    width = float(input())
    
    return width

# Main
# This is a program to determine paint needs for a square room.
length = getRoomLength()
width = getRoomWidth()
height = getRoomHeight()
paintCoverage = getPaintCoverage()
price = getPrice()
area = calculateArea(length, width, height)
paint = calculatePaint(area, paintCoverage)
cost = calculateCost(paint, price)
displayResults(cost, paint)
