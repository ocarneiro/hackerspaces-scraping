# coding: utf-8
from collections import namedtuple
import csv
import re

h = namedtuple('Hackerspace', 'name name2 country state city site date_str status date_num')

# TODO: change to with
csvfile = open('hackerspaces_alll_2017_01_22.csv', newline='')
reader = csv.reader(csvfile)
hackerspaces = []

for row in reader:
    hackerspaces.append(h(*row[0:9])) 
    
active = [h for h in hackerspaces if h.status == 'active']
with_site = [h for h in active if len(h.site) > 2 ]

sites = [h.site for h in with_site]
# or sites = [h.site for h in active if len(h.site)>2]

distinct_sites = set(sites)

sites = {}
for h in distinct_sites:
    n = re.search('https*://(.*)', h)
    if n is not None:
        filename = n.group(1).replace('.','_').replace('/','') + '.txt'
        d = {"filename": filename }
        sites[h] = d
    else:
        print(h)

with open('sites.json', 'w') as arqjson:
    print(json.dumps(sites), file=arqjson)
