# This is a program that parses XML, processes, and formats it


import xml.etree.cElementTree as ET
import sys


def input_xml():
    test = ET.parse('https://www.w3schools.com/xml/plant_catalog.xml')
    data = test.getroot()
    print(data.tag)
    for line in data:
        print(data.find('name').text)

input_xml()
