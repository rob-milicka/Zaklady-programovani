vrstva01 = iface.activeLayer ()
prvky = vrstva01.getFeatures()
print "Zacatek vypisu"
print
for f in prvky:
    print "ID =", f.id() 
    a=f.geometry() 
    print "Typ prvku = ", a.type()
    if a.type()==0:
        #print"OO"
        print "Poloha = ", a.asPoint()
    elif a.type()==1:
        #print "XX"
        b=a.asPolyline()
        print "Pocet bodu linie =", len(b)
        print "Vypis bodu =", b
    elif a.type()==2:
        c=a.asPolygon()
        i=j=0
        print "Polygon ma", len(c), "okruhu"
        for u in c:
            i=i+1
            j=len(u)
            print i,". okruh ma", len(u)-1, "lomovych bodu"
            print "Seznam bodu", i,". okruhu =",u
        
        print "Polygon ma celkem ",j-1,"lomovych bodu"
    else: print "Nezmamy typ"
    
    
    atr = f.attributes()
    print "Atributy = ", atr
print
print "Konec vypisu"
