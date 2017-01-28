# coding: utf-8
from bs4 import BeautifulSoup as bs
import requests
import csv

filename = 'hackerspaces2000.csv'

url = 'https://wiki.hackerspaces.org/Special:Ask/-5B-5BCategory:Hackerspace-5D-5D/-3F=Hackerspace-23/-3F=Hackerspace-23/-3F=Hackerspace-23/-3FCountry/-3FState/-3FCity/-3FWebsite/-3FDate-20of-20founding/-3FHackerspace-20status/format=broadtable/limit=500/sort=Date of founding/mainlabel=Hackerspace/offset=2000'
r = requests.get(url)
soup = bs(r.text, 'html.parser')
t = soup.table
classes = 'Hackerspace,Hackerspace#,Country,State,City,Website,Date-of-founding,Hackerspace-status,data-sort-value'.split(',')

with open(filename, 'w', newline='') as csvfile:
    mywriter = csv.writer(csvfile, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
    # escreve os nomes dos campos no cabeçalho do arquivo csv
    mywriter.writerow(classes)

    trs = t.find_all('tr')

    for tr in trs:
        current_line = []
        tds = tr.find_all('td')
        for i in range(8):
            current_line.append(tds[i].text)
        if tds[6].has_attr('data-sort-value'):
            current_line.append(tds[6]['data-sort-value'])
        mywriter.writerow(current_line)
