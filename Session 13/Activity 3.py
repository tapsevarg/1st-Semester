# This is a program to process comma separated lists


def input_values():
    print("Please enter your comma-separated-values")
    values = input()
    return values


def process_values(values):
    values = values.replace(" ", "")
    records = values.split(",")
    records = list(filter(None, records))
    return records


def output_records(records):
    for elements in records:
        print(elements)


def main():
    values = input_values()
    records = process_values(values)
    output_records(records)


main()
