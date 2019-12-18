"""
Fonction qui renvoie le nombre de diviseur d'un entier
"""

"""Fonctions"""
def nombreDeDiviseurs(max):
    n = 0
    for i in range(1, max+1):
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += 1
        if c >= 7:
            n += 1
        c = 0
    return n


#exemple
print(nombreDeDiviseurs(30))
