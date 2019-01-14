import plotly
import plotly.plotly as py
import plotly.graph_objs as go

#py.sign_in('wojteksz128', 'Zw2M9roJ1Kp3YDyURXE3')

file = open('pan-tadeusz.txt', encoding='utf-8')
tekst = file.read()
#tekst.replace("\n", " ").replace("\t", " ").replace("  ", " ")
print(tekst.split(" "))
