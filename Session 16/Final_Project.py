# This is a program that parses XML, processes, and formats it


import re
import urllib.request
import sys


def input_xml():
    info = []
    source = urllib.request.urlopen("http://www.google.com")
    with open("source", "r") as file:
    
