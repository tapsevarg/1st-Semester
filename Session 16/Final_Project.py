# This is a program that parses XML, processes, and formats it


import urllib.request
import xml.etree.ElementTree


def input_xml():
    commons = []
    botanicals = []
    zones = []
    lights = []
    prices = []
    availabilities = []
    url = "https://www.w3schools.com/xml/plant_catalog.xml"
    try:
        page = urllib.request.urlopen(url).read()
        page = page.decode("UTF-8")
    except Exception as exception:
        print(str(exception) + " reading " + url)
        exit(1)
    info = xml.etree.ElementTree.fromstring(page)
    data = xml.etree.ElementTree.ElementTree(info)
    for element in data.iter():
        print("%s: %s" % (element.tag, element.text))
 

input_xml()
