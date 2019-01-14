from pyx import *

import csv
import re

eur_dates = []
eur_values = []

with open('EUR.n_20161028_20161128.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    value = 0
    for row in spamreader:
        if len(row) < 4 or re.match("^\d+?\,\d+?$", row[2]) is None:
            continue
        print (row)
        eur_dates.append(row[1])
        eur_values.append(float(str(row[2]).replace(',', '.')))

eur_dates.reverse
eur_values.reverse
print (eur_dates)
print (eur_values)

g = graph.graphxy(width=8)
g.plot(graph.data.values(x=list(range(0, len(eur_values))), y=eur_values))

g.writePDFfile("zadanie_1")
