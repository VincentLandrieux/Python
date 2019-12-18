# -*- coding: utf-8 -*-


"""import"""
import random
import tkinter as tk

"""variables"""
#Constante
lignes = 10 # Nombre de ligne dans la matrice
colonnes = 10 # Nombre de colonne dans la matrice
nbCels = 33 # Nombre de cellule initiales

nbTour = 100 # Nombre de tour

sleep = 0.1 # Temps de latence du rafraîchissement (en seconde)


matrice = []

k = nbCels 
c = 0

# Variable Canvas
longeurCanvas = 800 # Longeur du canvas
largeurCanvas = 800 # Hauteur du canvas


lo = (longeurCanvas/colonnes) # Longeur d'une case
la = (largeurCanvas/lignes) # Hauteur d'une case

fenetre = tk.Tk()
canvas = tk.Canvas(fenetre, width=longeurCanvas, height=largeurCanvas)

matriceDraw = []


"""fonctions"""
def comptCellAround(m, x, y):
    # Compte le nombre de cellule adjacente
    c = 0
    for i in [[x-1, y-1], [x, y-1], [x+1, y-1], 
              [x-1, y], [x+1, y],
              [x-1, y+1], [x, y+1], [x+1, y+1]]:
        if((0 < i[0] < len(m[0])) and (0 < i[1] < len(m))):
            if(m[i[1]][i[0]] == 1):
                c += 1
    return c
    
def verifCrea(m, x, y):
    # Vérifie si il faut créer une cellule en coordonées x, y
    f = False
    c = comptCellAround(m, x, y)
    
    if c >= 3:
        f = True
    
    return f
    
def verifSuppr(m, x, y):
    # Vérifie si il faut détruire une cellule en coordonées x, y
    f = False
    c = comptCellAround(m, x, y)
    if c < 2:
        f = True
    elif c >= 4:
        f = True
    
    return f

def majMatrice(matrice):
    # Rafraîchit les donnée de la matrice 
    chang = []
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if(matrice[i][j] == 0):
                if(verifCrea(matrice, j, i)):
                    chang.append([i,j])
            else:
                if(verifSuppr(matrice, j, i)):
                    chang.append([i,j])
    
    for i in chang:
        if matrice[i[0]][i[1]] == 0:
            matrice[i[0]][i[1]] = 1
        else:
            matrice[i[0]][i[1]] = 0

def majMatriceDraw(matrice, matriceDraw):
    # Rafraîchit les données de la matrice d'affichage
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if(matrice[i][j] == 1):
                canvas.itemconfig(matriceDraw[i][j], fill = "blue")
            else:
                canvas.itemconfig(matriceDraw[i][j], fill = "white")

def affichageMatrice(matrice):
    # Affiche la matrice dans la console
    print("\033[H\033[J")# Clear console
    
    for i in range(len(matrice[0])):
        for j in range(len(matrice)):
            print(matrice[j][i], end=" ")
        print()
    print("\n")

    
def comptCels(matrice):
    c = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if(matrice[i][j] == 1):
                c += 1
    return c

def start():
    global buttonStart
    buttonStart.destroy()
    maj()

def maj():
    #Rafraîchissement Global
    global sleep
    global nbTour
    global c
    
    c += 1
    compteur['text'] = str(c)+" /"+str(nbTour)
    compteurCels['text'] = "Nb cell: " + str(comptCels(matrice))
    
    # Maj Matrice
    majMatrice(matrice)
    # Maj Matrice Draw
    majMatriceDraw(matrice, matriceDraw)
    # Affichage de la matrice
    #affichageMatrice(matrice)
    
    if( c < nbTour):
        fenetre.after(int(sleep*1000), maj)

    

"""main"""
# Initialisation de la matrice
    #i = x, j =y
for i in range(colonnes):
    matrice.append([])
    for j in range(lignes):
        matrice[i].append(0)
    
# Generation des cellules 
while k > 0:
    i = random.randint(0, colonnes-1)
    j = random.randint(0, lignes-1)
    if matrice[i][j] == 0:
        matrice[i][j] = 1
        k -= 1

        
# Initialisation matrice affichage
for i in range(colonnes):
    matriceDraw.append([])
    for j in range(lignes):
        x = i*lo
        y = j*la
        x2 = i*lo+lo
        y2 = j*la+la

        matriceDraw[i].append(canvas.create_rectangle(x, y, x2, y2))
        #canvas.create_text(x+lo/2,y+la/2, text= str(i)+","+str(j))

majMatriceDraw(matrice, matriceDraw)
#affichageMatrice(matrice)

buttonStart = tk.Button(fenetre, text='start', command=start)
compteur = tk.Label(fenetre, text=str(c)+" /"+str(nbTour))
compteurCels = tk.Label(fenetre, text="Nb cell: " + str(comptCels(matrice)))

buttonStart.pack()
compteur.pack()
compteurCels.pack()
canvas.pack()

fenetre.mainloop()



