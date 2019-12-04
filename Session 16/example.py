# This is a program that parses XML, processes, and formats it


import urllib.request
import xml.etree.ElementTree


def get_data(url):
    try:
        page = urllib.request.urlopen(url).read()
        page = page.decode("UTF-8")
    except Exception as exception:
        print("Error reading " + url)
        print(str(exception))
        exit(1)
    info = xml.etree.ElementTree.fromstring(page)
    data = xml.etree.ElementTree.ElementTree(info)
    return data


def get_tag(data, tag):
    array = []
    for child in data.iter(tag):
        array.append(child.text)
    return array


def get_total(common, botanical, zone, light, price):
    if len(common) == 0:
        print("Error with values extracted from XML")
        exit(1)

    test = (len(common), len(botanical), len(zone), len(light), len(price))
    if(len(set(test))==1):
        total = test[0]
        return total
    else:
        print("Error with values extracted from XML")
        exit(1)


def process_price(price):
    try:
        for i in range(len(price)):
            price[i] = float(price[i].replace("$", ""))

        average = sum(price) / len(price)
        average = round(average, 2)
        return average
    except:
        print("Expected dollar value is not numeric")
        exit(1)


def output_data(common, botanical, zone, light, price):
    for i in range(len(common)): 
        print(f'{common[i]} ({botanical[i]}) - {zone[i]} - {light[i]} - {price[i]}') 


def output_totals(total, average):
    print("The total number of items are " + str(total) + ".")
    print("The average price is $" + str(average) + ".")


def main():
    url = "https://www.w3schools.com/xml/plant_catalog.xml"
    data = get_data(url)

    common = get_tag(data, "COMMON")
    botanical = get_tag(data, "BOTANICAL")
    zone = get_tag(data, "ZONE")
    light = get_tag(data, "LIGHT")
    price = get_tag(data, "PRICE")

    total = get_total(common, botanical, zone, light, price)
    average = process_price(price)

    output_data(common, botanical, zone, light, price)
    output_totals(total, average)


main()
