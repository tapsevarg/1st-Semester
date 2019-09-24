# This is a program that calculates age measured in seconds, minutes, hours,
# days, and months


def get_age():
    print("How many years old are you?")
    age = int(input())
    return age


def calculate_seconds(age):
    seconds = (age) * 31536000
    return seconds


def calculate_minutes(age):
    minutes = (age) * 525600
    return minutes


def calculate_hours(age):
    hours = (age) * 8760
    return hours


def calculate_days(age):
    days = (age) * 365
    return days


def calculate_months(age):
    months = int(age) * 12
    return months


def display_results(age, seconds, minutes, hours, days, months):
    print("You have existed for more than")
    print("... " + str(seconds) + " seconds")
    print("... " + str(minutes) + " minutes")
    print("... " + str(hours) + " hours")
    print("... " + str(days) + " days")
    print("... " + str(months) + " months")


def main():
    age = get_age()
    seconds = calculate_seconds(age)
    minutes = calculate_minutes(age)
    hours = calculate_hours(age)
    days = calculate_days(age)
    months = calculate_months(age)
    display_results(age, seconds, minutes, hours, days, months)

main()
