#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time

url = "https://www.cnbcindonesia.com/investment"
headers = {'User-Agent': "encrypt0r-OS v6.66"}
req = requests.get(url=url, headers=headers)

soup = BeautifulSoup(req.text, "html.parser")
table = []

for xx in soup.findAll('h2'):
    if xx.find(class_='cbltv__title'):
        continue
    table += xx


print("<================================================>")
print("                   CNBC Scraper")
print("<================================================>")
print(f"Waktu : {time.ctime()}")
query = str(input("Ketik sebuah Keyword >> "))
print("<================================================>")
for xx in table:
    if query.lower() in xx.lower():
        print(xx)
    else:
        continue