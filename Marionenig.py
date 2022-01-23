import time,sys       #on importe le modultemps
import pickle
import pygame
import math
from pygame.locals import *
from random import randrange






pygame.init()



def creer_message(self, font, message, message_rectangle, couleur):


# ou gestion du temps






  if isclicking:                    #Définit les accélérations de balle
    if currentspeed < highestspeed:
      currentspeed = currentspeed + acceleration
    else :
      if currentspeed > lowestspeed:
        currentspeed = currentspeed - decceleration
      else:
        currentspeed = lowestspeed
  return currentspeed

def ballmoves(x,y,speed,mousepos):
  angle = (mousepos[0]-x,mousepos[1]-y)
  distanceballmouse = (mousepos[0]-x,mousepos[1]-y)/50
  if distanceballmouse > 1:
    distanceballmouse = 1
    vecteur[0] = sin(angle) * distanceballmouse
    vecteur[1] = cos(angle) * distanceballmouse
    x= x + vecteur[0]*speed
    y= y + vecteur[1]*speed
  return x,y
def update(self):
                newpos = self.calcnewpos(self.rect,self.vecteur)
                self.rect=newpos,(angle,z) = self.vecteur


tab=    [['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m'],                     #on cree la matrice
         ['m','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','c','m'],
         ['m','c','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','m'],
         ['m','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','m'],
         ['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m']]



largueur = len(tab[0])*64 # création de la fenetre de jeu
hauteur = len(tab)*64
fenetre = pygame.display.set_mode((largueur, hauteur))  # charger une image

fond = pygame.image.load("fond.png").convert_alpha()
fenetre.blit(fond, (0,0))
pygame.display.flip()
(x_mouse_save,y_mouse_save) = pygame.mouse.get_pos()
coordballe = [150,100] # coordonnée de la balle
vecteur = [1,1]
speed=0
continuer = True

while continuer ==True:
    print(coordballe)
    fenetre.blit(fond, (0,0)) # ajouter a la fenetre le fond

    bille = pygame.image.load("balle.png").convert_alpha() # afficher la balle dans l'écran
    fenetre.blit(bille,(coordballe[0],coordballe[1]))# ajouter à la fenetre la bille
    mouseinput = pygame.mouse.get_pressed()
    if mouseinput[0] :
      mousepos = pygame.mouse.get_pos()
      coordballe[0], coordballe[1] = ballmoves(coordballe[0],coordballe[1],speed,mousepos)

    balleRandomX = randrange(1, 5)
    balleRandomY = randrange(1, 5) #creation d'une valeur aleatoire pour la vitesse en Y

pygame.event.clear()
fenetre.fill(0) # efface la fenetre


position_balle.x += balleRandomX #on addition la valeur aleatoire a la position actuelle de la balle
position_balle.y += balleRandomY

if position_balle.left >= fenetreWidth or position_balle.right <= 0 :
     balleRandomX = -balleRandomX
if position_balle.bottom >= fenetreHeight or position_balle.top <= 0:
    balleRandomY = -balleRandomY

    #Re-collage
    fenetre.blit(balle, position_balle)
    #Rafraichissement
    pygame.display.flip()

    print(position_balle.topleft)



    # Si la balle touche les cotes, on inverse la variable concernee pour qu'elle change de cote
if position_balle.left >= fenetreWidth or position_balle.right <= 0 :
    balleRandomX = -balleRandomX
if position_balle.bottom >= fenetreHeight or position_balle.top <= 0:
    balleRandomY = -balleRandomY




mur = pygame.image.load("mur.png").convert_alpha() #afficher le mur dans l'écran
coffre = pygame.image.load("coffre.png").convert_lpha() # afficher le coffre dans l'ecran
for i in range(0,len(tab)) :
   for j in range(0,len(tab[0])) :
    if tab [i][j]=='m' :
      fenetre.blit(mur,(j*64,i*64))
      if tab [i][j] =='c' :
        fenetre.blit(coffre,(j*64,i*64))*6 #ajouter a la fenetre le coffre

def niveau_joueur(event):

    if event.key == K_F1:  #Choix f1 pour changer de niveau
      continuer_acceuil = 0
    choix = 'n1'



    event.key == K_F2 #Choix f2 pour changer de niveau


    choix = 'n2'

    if niveau.structure [dk.case_y] [dk.case_x] == 'a' :

        continuer_jeu = 0

##### FIN DU JEUX ####
    for event in pygame.event.get():                    #evenements de clavier
     if event.type == QUIT:


  #Rafraichissement
         pygame.display.flip()


continuer = False # quand on appuie on ferme la page
while not continuer:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              continuer = True
if continuer ==False:
      pygame.quit()
      sys.exit()

