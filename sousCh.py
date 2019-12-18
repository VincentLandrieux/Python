"""
Fonction de recupération d'une sous chaine de caractère
"""

#ch: chaine initiale
#d: index de départ
#f: index de fin exclu
"""Fonction"""
def sousCh(ch, d, f):
    sCh = ""
    if d < 0:
        d = 0
    if f >= len(ch):
        f = len(ch)
        
    for i in range(d,f):
        sCh += ch[i]
    
    return sCh

#Exemple
print(sousCh("abcdefg",2, 5)) #"cde"