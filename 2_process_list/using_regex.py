# coding: utf-8
names = []
for h in distinct_sites:
    n = re.search('https*://(.*)', h)
    if n is not None:
        names.append(n.group(1))
    else:
        print(h)
        
