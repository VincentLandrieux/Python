
"""Variables"""
tab = [100,57,86,39,92,34]

"""Fonctions"""
def SwitchTab(t,a,b):
    x = t[b]
    t[b] = t[a]
    t[a] = x


"""Calcul"""
print("tab=",tab)

for i in range(len(tab)-1,0,-1):
    print("\n"+"i =",i)
    for j in range(0,i):
        print(" j =",j)
        if(tab[j+1] < tab[j]):
            SwitchTab(tab, j+1, j)
        print("  tab=",tab)
