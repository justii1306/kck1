import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.plotly as py

#py.sign_in('wojteksz128', 'Zw2M9roJ1Kp3YDyURXE3')

plotly.offline.plot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})
