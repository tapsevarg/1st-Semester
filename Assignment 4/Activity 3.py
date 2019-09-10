# This is a program to calculate kilometers, meters, and centimeters based on a mileage input.

print ("Enter number of miles to convert")
miles = float(input())

kilometers = (miles)*1.609344
meters = (miles)*1609.34
centimeters = (miles)*160934

print (str(miles) + " miles converts to " + str(kilometers) + " kilometers, " + str(meters) + " meters, and " + str(centimeters) + " centimeters.")