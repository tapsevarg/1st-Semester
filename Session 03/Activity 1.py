def toFixed(value, digits):
    return "%.*f" % (digits, value)

# This program is a calculator to extrapolate weekly, monthly, and yearly gross pay
print("Enter hours worked during week")
hours = float(input())
print("Enter rate of pay")
pay = float(input())
weekly = toFixed(hours * pay,2)
monthly = toFixed(hours * pay * 4.33333333333333,2)
yearly = toFixed(hours * pay * 52,2)
print("Weekly gross pay is $" + weekly)
print("Monthly gross pay is $" + monthly)
print("Yearly gross pay is $" + yearly)
