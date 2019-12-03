# This is a program that parses XML, processes, and formats it


import urllib.request
import xml.etree.ElementTree
import numpy as np
from itertools import zip_longest


def input_xml():
    source = {'common': [], 'botanical': [], 'zone': [], 'light': [], 'price': []}
    url = "https://www.w3schools.com/xml/plant_catalog.xml"
    try:
        page = urllib.request.urlopen(url).read()
        page = page.decode("UTF-8")
    except Exception as exception:
        print("Error reading " + url)
        print(str(exception))
        exit(1)
    info = xml.etree.ElementTree.fromstring(page)
    data = xml.etree.ElementTree.ElementTree(info)
    for child in data.iter("COMMON"):
        source['common'].append(child.text)
    for child in data.iter("BOTANICAL"):
        source['botanical'].append(child.text)
    for child in data.iter("ZONE"):
        source['zone'].append(child.text)
    for child in data.iter("LIGHT"):
        source['light'].append(child.text)
    for child in data.iter("PRICE"):
        source['price'].append(child.text)
    return source
 

def test_xml(source):
    if '' in source:
        print("Error with values extracted from XML")
        exit(1)
    else:
        pass
    test = [len(v) for v in source.values()]
    if(len(set(test))==1):
        total = test[0]
        return total
    else:
        print("Error with values extracted from XML")
        exit(1)


def process_xml(source, total):
    money = []
    for key in source.keys():
        money.append(source[key])
    dollars = (money[4])
    dollars = [peso.replace('$', '').replace(' ', '') for peso in dollars]
    try:
        dollars = np.array(dollars,float)
    except:
        print("Expected dollar value is not numeric")
        exit(1)
    average = sum(dollars) / len(dollars)
    average = round(average, 2)
    return average


def output_xml(source, total, average):
    output = ([i for t in zip_longest(*[source[k] for k in sorted(source)])
          for i in t if i is not None])
    for i in range(0, len(output), 5): 
        print('{} ({}) - {} - {} - {}'.format(*output[i:i+5])) 
    print("The total number of items are " + str(total) + ".")
    print("The average price is $" + str(average) + ".")


def main():
    source = input_xml()
    total = test_xml(source)
    average = process_xml(source, total)
    output_xml(source, total, average)


main()
