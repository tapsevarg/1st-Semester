# This program is a calculator to extrapolate weekly, monthly,
# and yearly gross pay


def get_hours():
    print("Enter hours worked during week")
    hours = float(input())
    return hours


def get_pay():
    print("Enter rate of pay")
    pay = float(input())
    return pay


def toFixed(value, digits):
    return "%.*f" % (digits, value)


def calculate_weekly(hours, pay):
    weekly = toFixed(hours * pay, 2)
    return weekly


def calculate_monthly(hours, pay):
    monthly = toFixed(hours * pay * 4.33333333333333, 2)
    return monthly


def calculate_yearly(hours, pay):
    yearly = toFixed(hours * pay * 52, 2)
    return yearly


def display_results(weekly, monthly, yearly):
    print("Weekly gross pay is $" + weekly)
    print("Monthly gross pay is $" + monthly)
    print("Yearly gross pay is $" + yearly)


def main():
    hours = get_hours()
    pay = get_pay()
    weekly = calculate_yearly(hours, pay)
    monthly = calculate_monthly(hours, pay)
    yearly = calculate_yearly(hours, pay)
    display_results(weekly, monthly, yearly)


main()
