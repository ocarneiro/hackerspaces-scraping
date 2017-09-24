# coding: utf-8
from bs4 import BeautifulSoup as bs
import requests
import csv

filename = 'active_hackerspaces_with_e-mail_0501-1000.csv'

# url = 'https://wiki.hackerspaces.org/Special:Ask/-5B-5BCategory:Hackerspace-5D-5D/-3F=Hackerspace-23/-3F=Hackerspace-23/-3F=Hackerspace-23/-3FCountry/-3FState/-3FCity/-3FWebsite/-3FDate-20of-20founding/-3FHackerspace-20status/format=broadtable/limit=10/sort=Country/mainlabel=Hackerspace/offset=300'

#url = 'https://wiki.hackerspaces.org/w/index.php?title=Special%3AAsk&q=%5B%5BCategory%3AHackerspace%5D%5D+%5B%5BHackerspace+status%3A%3Aactive%5D%5D+%5B%5BE-mail%3A%3A%2B%5D%5D&po=%3F%3DHackerspace%23%0D%0A%3FCountry%0D%0A%3FState%0D%0A%3FCity%0D%0A%3FWebsite%0D%0A%3FDate+of+founding%0D%0A%3FHackerspace+status%0D%0A%3FEmail%0D%0A&eq=yes&p%5Bformat%5D=broadtable&sort_num=&order_num=ASC&p%5Blimit%5D=5&p%5Boffset%5D=&p%5Blink%5D=all&p%5Bsort%5D=Country&p%5Bheaders%5D=show&p%5Bmainlabel%5D=Hackerspace&p%5Bintro%5D=&p%5Boutro%5D=&p%5Bsearchlabel%5D=...+further+results&p%5Bdefault%5D=&p%5Bclass%5D=sortable+wikitable+smwtable&eq=yes'

url = 'https://wiki.hackerspaces.org/w/index.php?title=Special:Ask&q=%5B%5BCategory%3AHackerspace%5D%5D+%5B%5BHackerspace+status%3A%3Aactive%5D%5D+%5B%5BE-mail%3A%3A%2B%5D%5D&p=format%3Dbroadtable%2Flink%3Dall%2Fheaders%3Dshow%2Fmainlabel%3DHackerspace%2Fsearchlabel%3D...-20further-20results%2Fclass%3Dsortable-20wikitable-20smwtable&po=%3F%3DHackerspace%23%0A%3FCountry%0A%3FState%0A%3FCity%0A%3FWebsite%0A%3FDate+of+founding%0A%3FHackerspace+status%0A%3FEmail%0A&sort=Country&limit=500&eq=no&offset=500'

r = requests.get(url)
soup = bs(r.text, 'html.parser')
t = soup.table

classes = 'Hackerspace,Hackerspace#,Country,State,City,Website,Date-of-founding,Hackerspace-status,Email'.split(',')

with open(filename, 'w', newline='') as csvfile:
    mywriter = csv.writer(csvfile, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
    # escreve os nomes dos campos no cabeçalho do arquivo csv
    mywriter.writerow(classes)  #+ ['data-sort-value'])

    trs = t.find_all('tr')

    for tr in trs:
        current_line = []
        tds = tr.find_all('td')
        for i in range(len(classes)):
            current_line.append(tds[i].text)
        mywriter.writerow(current_line)

