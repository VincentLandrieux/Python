"""
Fonction de génération d'un tableau
d: valeur de départ
f: valeur de fin exclue
s: valeur de l'indentation
"""
def RangeF(d,f,s):
    t = []
    i = d
    while i < f:
        t.append(i)
        i += s
        i = round(i, 7)
    return t

#Exemple
print(RangeF(0,1,0.1))