# This is a program to calculate sock size


def getShoes():
    print("Please enter shoe size")
    shoes = float(input())
    return shoes


def displayXsmall():
    print("Buy size extra small socks.")


def displaySmall():
    print("Buy size small socks.")


def displayMedium():
    print("Buy size medium socks.")


def displayLarge():
    print("Buy size large socks.")


def displayXlarge():
    print("Buy size extra large socks.")


def main():
    shoes = getShoes()
    if shoes < 4:
        displayXsmall()
    else:
        if shoes <= 6:
            displaySmall()
        else:
            if shoes <= 9:
                displayMedium()
            else:
                if shoes <= 12:
                    displayLarge()
                else:
                    displayXlarge()


main()
