# coding: utf-8
from bs4 import BeautifulSoup as bs
import requests
import csv

filename = 'hackerspaces.csv'

url = 'https://wiki.hackerspaces.org/Special:Ask/-5B-5BCategory:Hackerspace-5D-5D/-3F=Hackerspace-23/-3F=Hackerspace-23/-3F=Hackerspace-23/-3FCountry/-3FState/-3FCity/-3FWebsite/-3FDate-20of-20founding/-3FHackerspace-20status/format=broadtable/limit=10/sort=Country/mainlabel=Hackerspace/offset=300'
r = requests.get(url)
soup = bs(r.text, 'html.parser')
t = soup.table
classes = 'Hackerspace,Hackerspace#,Country,State,City,Website,Date-of-founding,Hackerspace-status'.split(',')

with open(filename, 'w', newline='') as csvfile:
    mywriter = csv.writer(csvfile, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
    # escreve os nomes dos campos no cabeçalho do arquivo csv
    mywriter.writerow(classes + ['data-sort-value'])

hackerspaces = []
trs = t.find_all('tr')

for tr in trs:
    current_hs = {}
    tds = tr.find_all('td')
    for i, key in enumerate(classes):
        current_hs[key] = tds[i].text
    current_hs['data-sort-value'] = tds[6]['data-sort-value']
    hackerspaces.append(current_hs)


    
