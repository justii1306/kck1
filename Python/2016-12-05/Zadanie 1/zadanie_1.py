import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from PIL import Image

#py.sign_in('wojteksz128', 'Zw2M9roJ1Kp3YDyURXE3')

def endOfClass(iloscKlas):
    elementsInClass = int(256 / iloscKlas)
    rest = [i+1 for i in range(int(256%iloscKlas))] + [int(256%iloscKlas) for i in range(iloscKlas - int(256%iloscKlas) - 1)]
    return [0] + [ elementsInClass*i+rest[i-1] for i in range(1, iloscKlas) ] + [256]

def groupBy(lista, ilosc):
    return [ lista[i:i+ilosc] for i in range(0, len(lista), ilosc) ]

def groupByClass(lista, iloscKlas):
    ends = endOfClass(iloscKlas)
    return [str(ends[i]) + " - " + str(ends[i+1] - 1) for i in range(iloscKlas)], [[sum([x[j] for x in lista[ends[i]:ends[i+1]]]) for j in range(3)] for i in range(iloscKlas)]

def inputValue(min, max):
    value = int(input("Podaj ilość grup histogramu (z przedziału " + str(min) + " - " + str(max) + "): "))
    return value

image = Image.open("do_skanowania.jpg")
x, y = groupByClass(groupBy(image.histogram(), 3), inputValue(1, 256))

trace1 = go.Bar(x=x,
                y=[i[0] for i in y],
                name='Czerwony',
                marker=dict(color='rgb(255,0,0)'))
trace2 = go.Bar(x=x,
                y=[i[1] for i in y],
                name='Zielony',
                marker=dict(color='rgb(0,255,0)'))
trace3 = go.Bar(x=x,
                y=[i[2] for i in y],
                name='Niebieski',
                marker=dict(color='rgb(0,0,255)'))

data = [trace1, trace2, trace3]
layout = go.Layout(barmode='group', title='Histogram pliku "do_skanowania.jpg"')
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='Histogram pliku do_skanowania.jpg.html')
#py.plot(fig, filename='Histogram pliku do_skanowania.jpg.html')
