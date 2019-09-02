# This is a program that calculates age measured in seconds, minutes, hours, days, and months
print("How many years old are you?")
age = int(input())
seconds = age * 31536000
minutes = age * 525600
hours = age * 8760
days = age * 365
months = age * 12
print("You have existed for more than " + str(seconds) + " seconds.")
print("... " + str(minutes) + " minutes")
print("... " + str(hours) + " hours")
print("... " + str(days) + " days")
print("... " + str(months) + " months")
