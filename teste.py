# coding: utf-8
from bs4 import BeautifulSoup as bs
import requests
url = 'https://wiki.hackerspaces.org/Special:Ask/-5B-5BCategory:Hackerspace-5D-5D/-3F%3DHackerspace-23/-3F%3DHackerspace-23/-3F%3DHackerspace-23/-3FCountry/-3FState/-3FCity/-3FWebsite/-3FDate-20of-20founding/-3FHackerspace-20status/format%3Dbroadtable/limit%3D100/sort%3DCountry/mainlabel%3DHackerspace/offset%3D100#'
r = requests.get(url)
soup = bs(r.text, 'html.parser')
t = soup.find_all("table")
len(t)
t = soup.table
cities = soup.find_all('td', class_='City')
for a in cities:
    print (a.text)
    
