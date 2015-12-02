import math
b = iface.activeLayer()
c = b.getFeatures()
for d in c:
        e = d.geometry()
        f = e.asPoint()
        nejvzdalenejsiLetiste = d['NAZEV']
        vzdalenostNejvzdalenejsihoLetiste = 0
        a = b.getFeatures()
        for n in a:
            souradnice = n.geometry()
            bod = souradnice.asPoint()
            h = f.x()
            i = f.y()
            vzdalenostx = f.x()-bod.x()
            vzdalenosty = f.y()-bod.y()
            vzdalenost = math.sqrt(vzdalenostx*vzdalenostx+vzdalenosty*vzdalenosty)
            if vzdalenostNejvzdalenejsihoLetiste<vzdalenost:
                vzdalenostNejvzdalenejsihoLetiste = vzdalenost
                nejvzdalenejsiLetiste = n['NAZEV']
        print d['NAZEV'], nejvzdalenejsiLetiste

