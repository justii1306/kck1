from PIL import Image
import plotly.plotly as py
import plotly.graph_objs as go

l = []

def groupBy(l, n):
    return [ l[i:i+n] for i in range(0, len(l), n) ]

image = Image.open("1.jpg")
histogram = groupBy(image.histogram(), 3)

data = [go.Bar(
            x=['R', 'G', 'B'],
            y=l
    )]

py.iplot(data, filename='basic-bar')
