import time,sys                                     #on importe le modultemps
import math
import pygame                                       #on importe pygame
from pygame.locals import *
import random

pygame.init()


tab=    [['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m'],                     #on cree la matrice
         ['m','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','c','m'],
         ['m','c','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','m'],
         ['m','b','b','b','b','b','b','c','b','b','b','b','b','b','b','b','b','b','b','m'],
         ['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m']]

largeur = len(tab[0])*64
hauteur = len(tab)*64
fenetre = pygame.display.set_mode((largeur, hauteur))       #Ouverture de la fenêtre Pygame

fond = pygame.image.load("fond.png").convert_alpha() #Chargement et collage du fond
fenetre.blit(fond, (0,0))                           # position du fond en (x,y) =(0,0)
pygame.display.flip()                               #actualisation ecran



(x_mouse_save,y_mouse_save) = pygame.mouse.get_pos()

continuer = True
vecballe = pygame.math.Vector2(1.5,1.5)
coordballe = pygame.math.Vector2(150,100)

vecteur = [1,1]
speed=1


def check_reflection(pos,vector):
    if (64<pos[0]< float(largeur-64)):
        print("in square x " + str(pos[0]) + " " + str((largeur-64)))
        newpos = pos + vector
        #print (newpos)
    if (64<pos[1]< float(hauteur-64)):
        print("in square y " + str(pos[1]) + " " + str((largeur-64)))
        newpos = pos[1] + vector[1]

    if (pos[0]<= 64 or pos[1] <= 64):
        newpos = pos + vector.reflect(vector)
    
    if (pos[0]>= float(largeur-64) or pos[1] >= float(hauteur-64)):
        newpos = pos + vector.reflect(vector)

    #print(newpos)
    return (newpos) 

#---------------------------------------------------------------
#BOUCLE INFINIE

print (largeur)
print (hauteur)
while continuer ==True:

    #Re-collage du fond afin d effacer l ancienne position des objets
    fenetre.blit(fond, (0,0))

    bille = pygame.image.load("balle.png").convert_alpha()  #Mise en place d'un perso
    fenetre.blit(bille,(coordballe[0],coordballe[1]))
    #Exemple de déplacement : Enlever la ligne ci-dessous, la balle sera fixe !
    coordballe=check_reflection(coordballe,vecballe)

    

    mouseinput = pygame.mouse.get_pressed()
    if mouseinput[0] :
      mousepos = pygame.mouse.get_pos()
      print(mousepos)
    pygame.event.clear()
    #fenetre.fill(0) # efface la fenetre

   

    mur = pygame.image.load("mur.png").convert_alpha()      #Mise en place d'un perso
    coffre = pygame.image.load("coffre.png").convert_alpha() # afficher le coffre dans l'ecran
    for i in range(0,len(tab)) :
        for j in range(0,len(tab[0])) :
            if tab [i][j]=='m' :
                fenetre.blit(mur,(j*64,i*64))
            if tab [i][j] =='c' :
                fenetre.blit(coffre,(j*64,i*64))#ajouter a la fenetre le coffre

    for event in pygame.event.get():                    #evenements de clavier
        if event.type == QUIT:                          #Si j'appuis sur le bouton echap
            continuer = False

    #Rafraichissement
    pygame.display.flip()

if continuer ==False:
    pygame.quit()
    sys.exit()


