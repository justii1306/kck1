from pyx import *
co = color.lineargradient_cmyk(color.cmyk.Blue, color.cmyk.LimeGreen);
c = canvas.canvas()
circ = path.circle(0, 0, 3)
c.stroke(circ, [style.linewidth.Thin, color.cmyk.Blue])
c.stroke(circ, [deco.filled([color.cmyk.Blue])])
c.fill(path.rect(0, 0, 1.5, 1.5), [color.cmyk.LimeGreen])
c.fill(path.rect(0, 0, -1.5, -1.5), [color.cmyk.Cerulean])
c.fill(path.rect(0, 0, -1.5, 1.5), [color.rgb.red])
c.fill(path.rect(0, 0, 1.5, -1.5), [color.cmyk.Yellow])
c.writeEPSfile()
c.writePDFfile()
c.writeSVGfile()