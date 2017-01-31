# coding: utf-8
import json
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

sites = {}
errors = {}

print("====== scrap_sites.py =======")
print("loading site list...")
with open('sites.json', 'r') as file:
    content = file.read()
    sites = json.loads(content)

print("scraping........")
for h in sorted(list(sites.keys())):
    print(h)
    try:
        r = requests.get(h)
        soup = bs(r.text, 'html.parser')
        with open(sites[h]['filename'],'w') as output:
            print(soup.text, file=output)
    except Exception as e:
        errors[h] = e

if any(errors):
    print("saving errors")
    with open("errors.log", "w") as output:
        pprint(errors, stream=output)

print("done!")
