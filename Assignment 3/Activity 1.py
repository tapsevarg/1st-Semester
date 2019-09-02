def toFixed(value, digits):
    return "%.*f" % (digits, value)

# This program is a calculator to extrapolate weekly, monthly, and yearly gross pay
print("Enter hours worked during week")
hours = float(input())
print("Enter payrate")
payrate = float(input())
weekly = toFixed(hours * payrate,2)
monthly = toFixed(hours * payrate * 4.33333333333333,2)
yearly = toFixed(hours * payrate * 52,2)
print("Weekly gross pay is $" + weekly)
print("Monthly gross pay is $" + monthly)
print("Yearly gross pay is $" + yearly)
