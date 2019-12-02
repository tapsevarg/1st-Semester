# This is a program that parses XML, processes, and formats it


import urllib.request
import xml.etree.ElementTree


def input_xml():
    source = {'common': [], 'botanical': [], 'zone': [],
              'light': [], 'price': [], 'availability': []}
    url = "https://www.w3schools.com/xml/plant_catalog.xml"
    try:
        page = urllib.request.urlopen(url).read()
        page = page.decode("UTF-8")
    except Exception as exception:
        print(str(exception) + " reading " + url)
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
    for child in data.iter("AVAILABILITY"):
        source['availability'].append(child.text)
    return source
 

def test(source):
    key_to_value_lengths = {k:len(v) for k, v in source.items()}
    print(key_to_value_lengths)


source = input_xml()
test(source)
