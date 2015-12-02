import math
b = iface.activeLayer()
c = b.getFeatures()
for d in c:
        e = d.geometry()
        f = e.asPoint()
        vzdalenostNejvzdalenejsihoLetiste = 500000
        a = b.getFeatures()
        for n in a:
            souradnice = n.geometry()
            bod = souradnice.asPoint()
            vzdalenostx = f.x()-bod.x()
            vzdalenosty = f.y()-bod.y()
            vzdalenost = math.sqrt(vzdalenostx*vzdalenostx+vzdalenosty*vzdalenosty)
            if (vzdalenostNejvzdalenejsihoLetiste>vzdalenost)and(vzdalenost>0)and(n['STATUT_LET']=='I'):
                vzdalenostNejvzdalenejsihoLetiste = vzdalenost
                nejvzdalenejsiLetiste = n['NAZEV']
        print d['NAZEV'], nejvzdalenejsiLetiste

