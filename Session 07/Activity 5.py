# This is a program to calculate sock size


def get_shoes():
    print("Please enter shoe size")
    shoes = float(input())
    return shoes


def display_xsmall():
    print("Buy size extra small socks.")


def display_small():
    print("Buy size small socks.")


def display_medium():
    print("Buy size medium socks.")


def display_large():
    print("Buy size large socks.")


def display_xlarge():
    print("Buy size extra large socks.")


def main():
    shoes = get_shoes()
    if shoes < 4:
        display_xsmall()
    else:
        if shoes <= 6:
            display_small()
        else:
            if shoes <= 9:
                display_medium()
            else:
                if shoes <= 12:
                    display_large()
                else:
                    display_xlarge()


main()
