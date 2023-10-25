#!/usr/bin/python3
# coding: utf-8
from bs4 import BeautifulSoup
import requests
import sys
url=(sys.argv[1])
#url="https://www.swissinfo.ch/por/a-su%C3%AD%C3%A7a-defenderia-o-liechtenstein-no-caso-de-um-ataque-militar-/47798482"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.html.head.title.text).encode('utf-16').replace("'", "\"").replace(chr(0xef),"").replace(chr(0xbd),"").replace(chr(0xbf),"")
print(soup.html.head.title.text).encode('utf-16').replace("'", "\"")
