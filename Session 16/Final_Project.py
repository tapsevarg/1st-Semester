# This is a program that parses XML, processes, and formats it


import urllib.request
import xml.etree.ElementTree


def input_xml():
    commons = []
    botanicals = []
    zones = []
    lights = []
    prices = []
    avails = []
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
        commons.append(child.text)
    for child in data.iter("BOTANICAL"):
        botanicals.append(child.text)
    for child in data.iter("ZONE"):
        zones.append(child.text)
    for child in data.iter("LIGHT"):
        lights.append(child.text)
    for child in data.iter("PRICE"):
        prices.append(child.text)
    for child in data.iter("AVAILABILITY"):
        avails.append(child.text)
    print(commons, botanicals, zones, lights, prices, avails)
 

input_xml()
