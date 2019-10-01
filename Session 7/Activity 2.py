# This is a program that calculates age measured in seconds, minutes, hours,
# days, and months


def get_age():
    print("How many years old are you?")
    age = int(input())
    return age


def get_choice():
    print("Choose measure of time to convert age to: " +
          "press S for age is seconds, H for hours, " +
          "D for days, and M for months.")
    choice = input()
    return choice


def calculate_seconds(age):
    seconds = (age) * 31536000
    return seconds


def calculate_hours(age):
    hours = (age) * 8760
    return hours


def calculate_days(age):
    days = (age) * 365
    return days


def calculate_months(age):
    months = int(age) * 12
    return months


def display_seconds(seconds):
    print("You have existed for more than " +
          str(seconds) + " seconds")


def display_hours(hours):
    print("You have existed for more than " +
          str(hours) + " hours")


def display_days(days):
    print("You have existed for more than " +
          str(days) + " days")


def display_months(months):
    print("You have existed for more than " +
          str(months) + " months")


def main():
    age = get_age()
    choice = get_choice()
    if choice == "S" or choice == "s":
        seconds = calculate_seconds(age)
        display_seconds(seconds)
    elif choice == "H" or choice == "h":
        hours = calculate_hours(age)
        display_hours(hours)
    elif choice == "D" or choice == "d":
        days = calculate_days(age)
        display_days(days)
    elif choice == "M" or choice == "m":
        months = calculate_months(age)
        display_months(months)
    else:
        null


main()
