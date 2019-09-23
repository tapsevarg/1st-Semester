# This program calculates the area of a rectangular room for ordering flooring.


def get_length():
    print("Enter length of room measured in feet")
    length = float(input())
    return length


def get_width():
    print("Enter width of room measured in feet")
    width = float(input())
    return width


def calculate_yards(length, width):
    yards = (length) * (width) / 9
    return yards


def display_results(yards):
    print(str("You need to order " + str(yards) +
          " square yard(s) of flooring."))


def main():
    length = get_length()
    width = get_width()
    yards = calculate_yards(length, width)
    display_results(yards)


main()
