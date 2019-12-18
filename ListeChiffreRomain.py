"""
Génération de chiffres romains
"""

"""Variables"""
chiffresRomain = ['XC','L','XL','X','IX','V','IV','I']
valeursRomain = [90,50,40,10,9,5,4,1]

maxi = 100

"""Fonctions"""
def Quantite(somme, valeur):
    return int(somme / valeur)

def TransRom(n):
    sR = ''
    for j in range(0,len(valeursRomain)):
        quantite = Quantite(n,valeursRomain[j])
        if(quantite > 0):
            sR += chiffresRomain[j] * quantite
        n -= quantite * valeursRomain[j]
    return sR

"""Entrer"""

"""Calcul"""
for i in range(1,maxi+1):
    print(i, '=', TransRom(i))
