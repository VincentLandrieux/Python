# -*- coding: utf-8 -*-
"""
Calcule la puissance seulement en addition
"""

"""Variables"""
a = 9
b = 4

"""Fonctions"""
def Multi(a,b):
    s = 0
    for i in range(b):
        s += a
    return s
    
def Puissance(a, b):
    if(b == 0):
        s = 1
    else:
        s = a
        for i in range(b-1):
            s = Multi(s,a)

    return s

"""Affichage"""
print(Puissance(a,b))
print(a**b)
