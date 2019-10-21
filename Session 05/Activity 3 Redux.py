# This program is a miles to kilometers, meters, and centimeters converter.


def get_miles():
    print("Enter number of miles to convert")
    miles = float(input())
    return miles


def calculate_kilometers(miles):
    kilometers = (miles) * 1.609344
    return kilometers


def calculate_meters(miles):
    meters = (miles) * 1609.34
    return meters


def calculate_centimeters(miles):
    centimeters = (miles) * 160934
    return centimeters


def display_results(miles, kilometers, meters, centimeters):
    print(str(miles) + " miles converts to " + str(kilometers) +
          " kilometers, " + str(meters) + " meters, and " + str(centimeters) +
          " centimeters.")


def main():
    miles = get_miles()
    kilometers = calculate_kilometers(miles)
    meters = calculate_meters(miles)
    centimeters = calculate_centimeters(miles)
    display_results(miles, kilometers, meters, centimeters)


main()
