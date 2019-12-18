
"""Variables"""
note = [8, 4, 12, 11, 9, 14, 19, 11, 19, 4, 18, 12, 19, 3, 5]

moyenne = None
mention = None

"""Fonctions"""
def NMin(tab):
    if(len(tab) > 0):
        m = tab[0]
        for i in range(1,len(tab)):
            if(m > tab[i]):
                m = tab[i]
    else:
        m = None
    
    return m

def NMax(tab):
    if(len(tab) > 0):
        m = tab[0]
        for i in range(1,len(tab)):
            if(m < tab[i]):
                m = tab[i]
    else:
        m = None
    
    return m

def Moyenne(tab):
    if(len(tab) > 0):
        m = tab[0]
        for i in range(1,len(tab)):
            m += tab[i]
        m /= len(tab)
    else:
        m = None
    
    return m
    

"""Calcul"""
moyenne = Moyenne(note)

if(moyenne < 10):
    mention = "redoublement"
elif(moyenne < 12):
    mention = "passable"
elif(moyenne < 14):
    mention = "assez-bien"
elif(moyenne < 16):
    mention = "bien"
else:
    mention = "très bien"

"""Affichage"""
print("Note maximum:", NMax(note))
print("Note minimum:", NMin(note))
print("Moyenne:", moyenne)
print("Mention:", mention)
