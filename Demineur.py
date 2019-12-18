# -*- coding: utf-8 -*-

"""import"""
import random
import tkinter as tk
#import time #Optionnel

"""variables"""
#Constante
taille = [10,20,30]
difficulte = [10,15,20]
lignes = 10 # Nombre de ligne dans la matrice
colonnes = 10 # Nombre de colonne dans la matrice
nbBomb = 10 # Nombre de bombe initiales

colors = ["white", "#ddd", "#ffc66e", "#f34200", "#6ee1ff", "#00c0f3", "#1888a5", "#0e5567", "#154e84"]
#        [ canvas,   case,   drapeau,      bomb,         0,         1,        2,          3,       >=4]

#sleep = 0.5 # Temps de latence du rafraîchissement (en seconde)

matrice = []
matriceDraw = []

play = False

# Variable Canvas
longeurCanvas = 600 # Longeur du canvas
largeurCanvas = 600 # Hauteur du canvas


loCase = (longeurCanvas/colonnes) # Longeur d'une case
haCase = (largeurCanvas/lignes) # Hauteur d'une case


fenetre = tk.Tk()
frame = tk.Frame(fenetre, width=longeurCanvas, height=largeurCanvas)

canvas = tk.Canvas(frame)

#Création du canvas Start
frameStart = tk.Frame(frame, bg= colors[0])

#Taille
frameTailleStart = tk.Frame(frameStart, bg = colors[0])
frameTailleStart.pack()
tailleCheck = tk.IntVar()
tailleCheck.set(taille[0])
tailleElements = []
#Difficulte
frameDifficulteStart = tk.Frame(frameStart, bg = colors[0])
frameDifficulteStart.pack()
difficulteCheck = tk.IntVar()
difficulteCheck.set(difficulte[0])
difficulteElements = []

#Création du canvas End
frameEnd = tk.Frame(frame, bg= colors[0])
textFrameEnd = None

caseRetournee= []
drapeaux = []


"""fonctions"""
def comptCellAround(m, x, y):
    canvas.itemconfig(matriceDraw[x][y][0], fill = colors[5])
    # Compte le nombre de cellule adjacente
    c = 0
    for i in [[x-1, y-1], [x, y-1], [x+1, y-1],
              [x-1, y], [x+1, y],
              [x-1, y+1], [x, y+1], [x+1, y+1]]:
        if((0 <= i[0] < len(m[0])) and (0 <= i[1] < len(m))):
            if(m[i[0]][i[1]] == 1):
                c += 1
    if c == 2:
        canvas.itemconfig(matriceDraw[x][y][0], fill = colors[6])
    if c == 3:
        canvas.itemconfig(matriceDraw[x][y][0], fill = colors[7])
    if c >= 4:
        canvas.itemconfig(matriceDraw[x][y][0], fill = colors[8])
                          
    return c

def goCellAround(m, x, y):#Optionnel
    #print(x,y, len(m))# A supprimer
    canvas.itemconfig(matriceDraw[x][y][0], fill = colors[4])
    #time.sleep(sleep)# A supprimer
    # Compte le nombre de cellule adjacente
    global caseRetournee
    c = 0
    for i in [[x-1, y-1], [x, y-1], [x+1, y-1],
              [x-1, y], [x+1, y],
              [x-1, y+1], [x, y+1], [x+1, y+1]]:
        if((0 <= i[0] < len(m[0])) and (0 <= i[1] < len(m))):
            if(caseRetournee.count([i[0], i[1]]) == 0):
                caseRetournee.append([i[0],i[1]])
                c = comptCellAround(m, i[0], i[1])
                canvas.itemconfig(matriceDraw[i[0]][i[1]][1], text=c)
                if c == 0:
                    goCellAround(m, i[0], i[1])

    return c

def poseDrapeaux(m,x,y):
    global drapeaux
    global nbBomb
    global caseRetournee
    global canvas
    
    if caseRetournee.count([x,y])==0:
        if drapeaux.count([x,y])==0:
            canvas.itemconfig(matriceDraw[x][y][0], fill = colors[2])
            drapeaux.append([x,y])
        else:
            canvas.itemconfig(matriceDraw[x][y][0], fill = colors[1])
            drapeaux.remove([x,y])
        nbDrapeaux=len(drapeaux) #Optionnel
        print("Bombe(s) restante(s) : "+str(nbBomb-nbDrapeaux)) #Optionnel

def affichageMatrice(matrice):
    # Affiche la matrice dans la console
    print("\033[H\033[J")# Clear console

    for i in range(len(matrice[0])):
        for j in range(len(matrice)):
            print(matrice[j][i], end=" ")
        print()
    print("\n")


def posMouse(o):
    x = o.winfo_pointerx() - o.winfo_rootx()
    y = o.winfo_pointery()- o.winfo_rooty()

    return [x,y]

def clickLeft(event):
    global matrice
    global canvas
    global loCase
    global haCase
    global lignes
    global colonnes
    global flag
    
    flag=False
    if play:
        x = int(posMouse(canvas)[0]//loCase)
        y = int(posMouse(canvas)[1]//haCase)
        caseRetournee.append([x,y])
        if(matrice[x][y] == 1):
            print("Bomb")
            canvas.itemconfig(matriceDraw[x][y][0], fill = colors[3])
            affichageFin()
        else:
            c=comptCellAround(matrice,x,y)
            canvas.itemconfig(matriceDraw[x][y][1], text=c)
            if c == 0:
                goCellAround(matrice, x, y)
    if len(caseRetournee) == (lignes*colonnes)-nbBomb:
        print("Terminé!")
        flag=True
        affichageFin()

def clickRight(event):
    global matrice
    global canvas
    global loCase
    global haCase
    
    if play:
        x = int(posMouse(canvas)[0]//loCase)
        y = int(posMouse(canvas)[1]//haCase)
        poseDrapeaux(matrice,x,y)

def affichageStart():
    global buttonStart
    global frameStart
    global frameEnd
    global play
    
    buttonStart["text"] = "Start"
    buttonStart["command"] = init
    
    frameEnd.place_forget()
    frameStart.place(x = longeurCanvas/10, y= largeurCanvas/10, width=longeurCanvas-(longeurCanvas/10)*2, height=largeurCanvas-(largeurCanvas/10)*2)
    play = False

def affichageFin():
    global textFrameEnd
    global flag
    global play
    
    if flag:
        textFrameEnd["text"] = "Gagné"
        
    else:
        textFrameEnd["text"] = "Perdu"
        
    play = False
        
    frameEnd.place(x = longeurCanvas/10, y= (largeurCanvas/10)*2, width=longeurCanvas-(longeurCanvas/10)*2, height=largeurCanvas-((largeurCanvas/10)*2)*2)
    

def firstclickLeft(event):
    global matrice
    global nbBomb
    global canvas
    global loCase
    global haCase
    
    matriceReset()
    generateBomb(matrice, nbBomb)
    affichageMatrice(matrice)
    
    x = int(posMouse(canvas)[0]//loCase)
    y = int(posMouse(canvas)[1]//haCase)
    flag =True
    while flag:
        if(matrice[x][y] == 1):
            matriceReset()
            generateBomb(matrice, nbBomb)
        else:
            flag = False
            clickLeft(None)
    
    canvas.bind("<Button-1>", clickLeft)

    
def matriceReset():
    # Initialisation de la matrice à 0
    global matrice
    global colonnes
    global lignes
    
    matrice = []
    #i = x, j =y
    for i in range(colonnes):
        matrice.append([])
        for j in range(lignes):
            matrice[i].append(0)
    
    affichageMatrice(matrice)

  
def generateBomb(m, b):
    while b > 0:
        i = random.randint(0, colonnes-1)
        j = random.randint(0, lignes-1)
        if matrice[i][j] == 0:
            matrice[i][j] = 1
            b -= 1

def init():
    global matrice
    global colonnes
    global lignes
    global nbBomb
    global matriceDraw
    global loCase
    global haCase
    global caseRetournee
    global drapeaux
    
    global tailleCheck
    global play
    
    global buttonStart
    global frameStart
    
    buttonStart["text"] = "Restart"
    buttonStart["command"] = affichageStart
    
    lignes = tailleCheck.get()
    colonnes = tailleCheck.get()
    nbBomb = ((lignes*colonnes)//100)*difficulteCheck.get()
    
    caseRetournee= []
    drapeaux = []
    
    #Cacher la frame start
    frameStart.place_forget()
    
    loCase = (longeurCanvas/colonnes) # Longeur d'une case
    haCase = (largeurCanvas/lignes) # Hauteur d'une case
    
    # Supression matrice affichage
    #canvas.delete(canvas.find_all())
    #print(canvas.find_all())
    for i in range(len(matriceDraw)):
        for j in range(len(matriceDraw[i])):
            canvas.delete(matriceDraw[i][j][0])
            canvas.delete(matriceDraw[i][j][1])
            
    # Initialisation matrice affichage
    matriceDraw = []
    for i in range(colonnes):
        matriceDraw.append([])
        for j in range(lignes):
            x = i*loCase
            y = j*haCase
            x2 = i*loCase+loCase
            y2 = j*haCase+haCase
    
            matriceDraw[i].append([canvas.create_rectangle(x, y, x2, y2, fill = colors[1]),
            canvas.create_text(x+loCase/2,y+haCase/2, text= "")])
    """
    # Rafraîchit les données de la matrice d'affichage
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            canvas.itemconfig(matriceDraw[i][j][0], fill = "")
            canvas.itemconfig(matriceDraw[i][j][1], text = "")
    """
    canvas.bind("<Button-1>", firstclickLeft)
    
    canvas.place(x = 0, y= 0, width=longeurCanvas, height=largeurCanvas)
    
    play = True
            
    


"""main"""

# Initialisation de la matrice
    #i = x, j =y
for i in range(colonnes):
    matrice.append([])
    for j in range(lignes):
        matrice[i].append(0)


# Initialisation matrice affichage
for i in range(colonnes):
    matriceDraw.append([])
    for j in range(lignes):
        x = i*loCase
        y = j*haCase
        x2 = i*loCase+loCase
        y2 = j*haCase+haCase

        matriceDraw[i].append([canvas.create_rectangle(x, y, x2, y2, fill = colors[1]),
        canvas.create_text(x+loCase/2,y+haCase/2, text= "")])
        
affichageMatrice(matrice)

buttonStart = tk.Button(fenetre, text='Start', command=init)


#Inputs
canvas.focus_set()
canvas.bind("<Button-1>", firstclickLeft)
canvas.bind("<Button-3>", clickRight)

#Création des éléments
#Frame Start
#Taille
tailleElements.append(tk.Label(frameTailleStart, text="Taille du tableau"))
tailleElements.append(tk.Radiobutton(frameTailleStart, text="Petit", bg="white", variable=tailleCheck, value=taille[0]))
tailleElements.append(tk.Radiobutton(frameTailleStart, text="Moyen", bg="white", variable=tailleCheck, value=taille[1]))
tailleElements.append(tk.Radiobutton(frameTailleStart, text="Grand", bg="white", variable=tailleCheck, value=taille[2]))
for i in range(len(tailleElements)):
    tailleElements[i].pack()
#Difficulte
difficulteElements.append(tk.Label(frameDifficulteStart, text="Difficulté"))
difficulteElements.append(tk.Radiobutton(frameDifficulteStart, text="Facile", bg="white", variable=difficulteCheck, value=difficulte[0]))
difficulteElements.append(tk.Radiobutton(frameDifficulteStart, text="Moyen", bg="white", variable=difficulteCheck, value=difficulte[1]))
difficulteElements.append(tk.Radiobutton(frameDifficulteStart, text="Difficile", bg="white", variable=difficulteCheck, value=difficulte[2]))
for i in range(len(difficulteElements)):
    difficulteElements[i].pack()
    
#Frame End
textFrameEnd = tk.Label(frameEnd, text="Perdu", anchor="center")
textFrameEnd.pack()


#Objects Pack
buttonStart.pack()

canvas.place(x = 0, y= 0, width=longeurCanvas, height=largeurCanvas)

frameStart.place(x = longeurCanvas/10, y= largeurCanvas/10, width=longeurCanvas-(longeurCanvas/10)*2, height=largeurCanvas-(largeurCanvas/10)*2)
frame.pack()


fenetre.mainloop()
