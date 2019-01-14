from pyx import *

c = canvas.canvas()
lines = []

circle = path.circle(0, 0, 2)
line = path.line(-1, -3, -1, 3)
c.stroke(circle, [style.linewidth.Thick])
c.stroke(line, [style.linewidth.Thick])

isects_circle, isects_line = circle.intersect(line)
for isect in isects_circle:
    isectx, isecty = circle.at(isect)
    lines.append(path.line(0, 0, isectx, isecty))
    c.stroke(lines[len(lines)-1])
    
isects_line.sort()
line1, line2, line3 = line.split(isects_line)


for centerline in lines:
    segment = line2 << centerline
    
c.fill(segment, [color.rgb.blue])
c.writePDFfile("zadanie_1")
