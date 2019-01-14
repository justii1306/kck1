from pyx import *
import math
import time


def drawCircleLine(kat):
    start = [0, 0]
    end = [0, 0]
    styles = []
    
    if kat % 30 == 0:
        start = [math.sin(math.radians(kat)) * 9.5, -math.cos(math.radians(kat)) * 9.5]
        end = [math.sin(math.radians(kat)) * 10.5, -math.cos(math.radians(kat)) * 10.5]
        styles = [style.linewidth(0.5)]
    else:
        start = [math.sin(math.radians(kat)) * 9.8, -math.cos(math.radians(kat)) * 9.8]
        end = [math.sin(math.radians(kat)) * 10.2, -math.cos(math.radians(kat)) * 10.2]

    c.stroke(path.line(start[0], start[1], end[0], end[1]), styles)

def drawTime(hour, minute, second):
    kat = [math.radians(30 * (hour % 12) + 30 * minute/60),
           math.radians(6 * minute),
           math.radians(6 * second)]

    length = [8, 9, 9]
    
    # Rysowanie wskazówki godzinowej
    c.stroke(path.line(0, 0, math.sin(kat[0]) * length[0], math.cos(kat[0]) * length[0]), [style.linewidth(1), style.linecap.round])
    # Rysowanie wskazówki minutowej
    c.stroke(path.line(0, 0, math.sin(kat[1]) * length[1], math.cos(kat[1]) * length[1]), [style.linewidth(0.7), style.linecap.round])
    # Rysowanie wskazówki sekundowej
    c.stroke(path.line(0, 0, math.sin(kat[2]) * length[2], math.cos(kat[2]) * length[2]), [color.rgb.red, style.linewidth(0.5), style.linecap.round])

def drawNumber(i):
    point = (math.sin(math.radians(30 * (i + 1))) * 8.8, math.cos(math.radians(30 * (i + 1))) * 8.8)
    c.text(point[0], point[1], i+1, [text.halign.boxcenter, text.size.Huge])

# Pole rysunkowe

# Zakładam, że tarcza zegara ma wymiary 50 x 50
c = canvas.canvas()

# c.stroke(path.path(path.arc(0, 0, 50, 0, 360)))
for i in [6*j for j in range(60)]:
    drawCircleLine(i)

for i in range(12):
    drawNumber(i)

t = time.localtime()
drawTime(t.tm_hour, t.tm_min, t.tm_sec)

c.writePDFfile("zegar")
