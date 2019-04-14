#!/usr/bin/env python3
import os

import time
import sys

import json
import urllib.request
from prettytable import PrettyTable

ORANGE="\033[93m"
RED="\033[91m"
GREEN="\033[92m"

INDEXES = ['name', 'net']

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def filterIndex(idx):
    if(idx in INDEXES):
        return True
    else:
        return False

def printOut(launches):
    printConfirmed(launches)
    printUnconfirmed(launches)
    return

def printConfirmed(launches):
    print(GREEN+"--- Next confirmed rocket launches ---\n")
    headers = filter(filterIndex, launches['launches'][0].keys())
    t = PrettyTable(headers)
    for i in launches["launches"]:
        if(i["status"] == 1):
            d2 = {k : v for k,v in filter(lambda t: t[0] in INDEXES, i.items())}
            list_values = [ v for v in d2.values() ]
            t.add_row(list_values)
    print(t)
    return

def printUnconfirmed(launches):
    print(ORANGE+"--- Next rocket launches ---\n")
    headers = filter(filterIndex, launches['launches'][0].keys())
    t = PrettyTable(headers)
    for i in launches["launches"]:
        if(i["status"] == 2 or i['status'] == 5):
            d2 = {k : v for k,v in filter(lambda t: t[0] in INDEXES, i.items())}
            list_values = [ v for v in d2.values() ]
            t.add_row(list_values)
    print(t)
    return
    

def main():

    urlData = ("https://launchlibrary.net/1.4/launch/next/15")

    clear()
    print('Collecting URL . . .')

    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()

    clear()

    encoding = webURL.info().get_content_charset('utf-8')
    launches = json.loads(data.decode(encoding))

    printOut(launches)

main()
