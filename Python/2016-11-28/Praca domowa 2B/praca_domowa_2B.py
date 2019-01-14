from pyx import *
from math import pi

# Dane wejściowe
outLine = 1.5
inLine = 1
r = 5

#Funkcja rysująca łuki
def drawArc(c, x, y, angle1, angle2, arcColor):
    c.stroke(path.path(path.arc(x, y, r, angle1, angle2)), [color.rgb.white, style.linewidth(outLine)])
    c.stroke(path.path(path.arc(x, y, r, angle1, angle2)), [arcColor, style.linewidth(inLine), style.linecap.round])

circle_1 = (color.rgb(0, 133/255, 199/255), 0, 0)
circle_2 = (color.rgb(244/255, 195/255, 0), r + outLine/2, -r)
circle_3 = (color.rgb.black, 2*r + outLine, 0)
circle_4 = (color.rgb(0, 159/255, 61/255), 3*r + 3/2*outLine, -r)
circle_5 = (color.rgb(223/255, 0, 36/255), 4*r + 2*outLine, 0)


c = canvas.canvas()
drawArc(c, circle_1[1], circle_1[2], 0, 335, circle_1[0])       # Pierwsze koło
drawArc(c, circle_2[1], circle_2[2], 0, 360, circle_2[0])       # Drugie koło
drawArc(c, circle_3[1], circle_3[2], 0, 360, circle_3[0])       # Trzecie koło
drawArc(c, circle_4[1], circle_4[2], 0, 360, circle_4[0])       # Czwarte koło
drawArc(c, circle_5[1], circle_5[2], 0, 360, circle_5[0])       # Piąte koło

drawArc(c, circle_2[1], circle_2[2], 65, 90, circle_2[0])       # Poprawienie przecięcia koła 2 z 3
drawArc(c, circle_1[1], circle_1[2], -25, 10, circle_1[0])      # Poprawienie przecięcia koła 1 z 2
drawArc(c, circle_4[1], circle_4[2], 65, 90, circle_4[0])       # Poprawienie przecięcia koła 4 z 5
drawArc(c, circle_3[1], circle_3[2], -25, 10, circle_3[0])      # Poprawienie przecięcia koła 3 z 4

c.writeSVGfile("circle")
