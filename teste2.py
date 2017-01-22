# coding: utf-8
tds = t.tr.find_all('td')
classes = []
for td in tds:
    classes.append(td['class'][0])
    
