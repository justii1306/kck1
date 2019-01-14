from math import sin, radians, pi
from pyx import *

def question(string:str, lista:list):
    string += ' [' + ' '.join([str(lista[i]) for i in range(len(lista))]) + ']: '
    inputData = input(string).split(' ')
    for i in range(len(inputData)):
        if inputData[i] == '':
            inputData.pop(i)
    return [ int(inputData[i]) for i in range(0, min(len(lista), len(inputData))) ] + lista[min(len(lista), len(inputData)) : len(lista)]

signal_1 = [2, 2]               # Parametry I   sygnału w kolejności - amplituda, częstotliwość
signal_2 = [2, 2, 0]            # Parametry II  sygnału w kolejności - amplituda, częstotliwość, opóźnienie (w stopniach)
signal_3 = [2, 3, 90]           # Parametry III sygnału w kolejności - amplituda, częstotliwość, opóźnienie (w stopniach)

signal_1 = question('Podaj parametry I sygnału (w kolejności amplituda, częstotliwość)', signal_1)
signal_2 = question('Podaj parametry II sygnału (w kolejności amplituda, częstotliwość, przesunięcie (w stopniach))', signal_2)
signal_3 = question('Podaj parametry III sygnału (w kolejności amplituda, częstotliwość, przesunięcie (w stopniach))', signal_3)

def lissajous(k):
    return signal_1[0] * sin(signal_1[1]*k), signal_2[0] * sin(signal_2[1]*k + radians(signal_2[2])), signal_3[0] * sin(signal_3[1]*k + radians(signal_3[2]))

g = graph.graphxyz(size=4, z=graph.axis.lin(min=-2))
g.plot(graph.data.paramfunction("k", 0, 2*pi, "x, y, z = f(k)", context={"f": lissajous}))
g.writePDFfile("lissajous")