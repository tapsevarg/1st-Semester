# This is a program for creating multiplication tables.


def get_value():
    print("Enter value to multiply")
    value = int(input())
    return value


def get_expressions():
    print("Choose number of expressions")
    expressions = int(input())
    return expressions


def process_math(value, expressions):
    count = 1
    while count <= expressions:
        result = value * count
        print(str(value) + " x " + str(count) + " = " + str(result))
        count += 1


def main():
    value = get_value()
    expressions = get_expressions()
    process_math(value, expressions)


main()
