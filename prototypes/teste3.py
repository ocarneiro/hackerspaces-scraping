# coding: utf-8
import csv
with open('classes.csv', 'w', newline='') as csvfile:
    mywriter = csv.writer(csvfile, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
    mywriter.writerow(classes)
    
