# This is a program that parses XML, processes, and formats it


import urllib.request
import xml.etree.ElementTree


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
    test = [len(v) for v in source.values()]
    if(len(set(test))==1):
        total = test[0]
        return total
    else:
        print("Error with values extracted from XML")
        exit(1)


def output_xml(source, total):
    keysValue = source.keys()
    for pack in zip(*source.values()): 
        print(dict(zip(keysValue, pack)))


source = input_xml()
total = test_xml(source)
output_xml(source, total)
