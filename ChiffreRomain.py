"""
Conversion d'un chiffre aléatoire en chiffre romain
"""

import random

"""Variables"""
chiffresRomain = ['C','XC','L','XL','X','IX','V','IV','I']
#                 100  90  50   40  10   9   5   4    1
valeursRomain = [100,90,50,40,10,9,5,4,1]
nb = [0,0,0,0,0,0,0,0,0]

nombre = round(random.random()*100)
nombreRomain = ''

print('Nombre:', nombre)
reste = nombre

"""Fonctions"""
def Quantite(somme, valeur):
    return int(somme / valeur)

"""Calcul"""
for i in range(0,len(chiffresRomain)):
    nb[i] = Quantite(reste, valeursRomain[i])
    reste -= nb[i] * valeursRomain[i]


"""Affichage"""
for i in range(0,len(chiffresRomain)):
    if(nb[i]>0):
        nombreRomain += nb[i]*chiffresRomain[i]

print(nombreRomain)
