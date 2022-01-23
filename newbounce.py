# coding: utf-8

import pygame, sys, time, os, json
from json2html import *
import random


######################################################################
##############################
###Définition des classes 
############################## 
######################################################################

############################## 
### Classe Balle qui se déplacera par une direction choisit par l'utilisateur
class Ball(pygame.sprite.Sprite):

    def __init__(self, startpos, velocity, startdir):
        super().__init__()
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()
        self.image = pygame.image.load("balle.png").convert_alpha()
        self.rect = self.image.get_rect(center = (round(self.pos.x), round(self.pos.y)))
        self.nextdir = None
    
    def reflect(self, NV):
        
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))
        if self.nextdir:
            self.nextdir=None

    def update(self):
        self.pos += self.dir * self.velocity
        self.rect.center = round(self.pos.x), round(self.pos.y)

    def moveleft(self):
        self.dir = pygame.math.Vector2(((self.dir.x-1),self.dir.y)).normalize()

    def moveright(self):
        self.dir = pygame.math.Vector2(((self.dir.x+1),self.dir.y)).normalize()

    def moveup(self):
        self.dir = pygame.math.Vector2((self.dir.x,(self.dir.y-1))).normalize()

    def movedown(self):
        self.dir = pygame.math.Vector2((self.dir.x,(self.dir.y+1))).normalize()

###################################
### Class Coffre
class Coffre(pygame.sprite.Sprite):
    def __init__(self, position,coord_j,coord_i):
        super().__init__()
        self.pos = pygame.math.Vector2(position)
        self.image = pygame.image.load("coffre.png").convert_alpha()
        self.rect = self.image.get_rect(center = (round(self.pos.x), round(self.pos.y)))
        self.tabj = coord_j
        self.tabi = coord_i

    def drawcoffrevide(self,fenetre):
        self.image = pygame.image.load("coffreVide.png").convert_alpha()
        fenetre.blit(self.image,self.rect)

    def drawcoffreferme(self,fenetre):
        self.image = pygame.image.load("coffre.png").convert_alpha()
        fenetre.blit(self.image,self.rect)


######################################################################
######################################################################
###################################
### Fonctions de Controle du jeux
###################################
######################################################################
######################################################################


### Page des records qui s'affiche une fois que le nombre de coffre vide totale a été atteint.
def record_page(start,end):
    record_page= True
    user_text =''
    fenetre.blit(fond, (0,0))                                   # position du fond en (x,y) =(0,0)
    while record_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                user_text+=event.unicode

                if event.key == pygame.K_RETURN:
                    write_file_record(user_text,second)
                    record_page = False
                if event.key == pygame.K_F9:
                    record_page = False
                    
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        print(str(start))
        print(str(end))
        second=end-start
        message_fenetre("Félicitation vous avez terminé en :", (0,0,0),(largeur/2),((hauteur/2)-20))
        message_fenetre(str(round(second)) + " secondes", (255,0,0),(largeur/2),((hauteur/2)+20))
        message_fenetre("Appuyer sur F9 pour Continuer ou ECHAPE pour Quitter", (0,0,0),(largeur/2),((hauteur/2)+80))
        text_surface = font.render(user_text,True, (255,255,255))

        message_fenetre("Saissez votre Nom",(255,0,0),(largeur/2),((hauteur/2)+35))
        fenetre.blit(text_surface,(((largeur/2)-50),((hauteur/2)+50)))
        pygame.display.update()
  
### Retourne un Rect à partir d'un font permettant de centrer le texte. 
def text_objects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

### Retroune un message centré dans la fenêtre
def message_fenetre(msg,color,posx,posy):
    textSurf, textRect = text_objects(msg,color)
    textRect.center = posx,posy
    fenetre.blit(textSurf, textRect)

### Definit le nombre de coffre dans une collection
def set_coffrecollection(tab):
    ### Faire une collection de Sprite Coffre
    collectCoffre =[]
    for i in range(0,len(tab)) :
        for j in range(0,len(tab[0])) :
                    if tab [i][j]=='c' :                          
                        collectCoffre.append(Coffre((j*64,i*64),j,i))
                        
                        
    ### Je vérifie le contenu de la liste 
    for i in range(0,len(collectCoffre)):
        print("List of Coffre in Collection, x:" + str(collectCoffre[i].pos.x) + " y:" + str(collectCoffre[i].pos.y))

    return collectCoffre

### Compte le nombre de coffres dans la collection
def count_coffre(collectcoffre):
    x=0
    for i in range(0,len(collectcoffre)) :
        x+=1
    return x


def init_niveau(niv):
    tab1=   [['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m'],                     
            ['m','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','m'],
            ['m','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','c','b','m'],
            ['m','b','b','c','b','b','b','c','b','b','b','b','b','b','b','b','b','b','b','m'],
            ['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m']]
    
    tab2=    [['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m'],                     
            ['m','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','m'],
            ['m','b','c','b','b','b','b','b','b','b','c','b','b','b','b','b','b','c','b','m'],
            ['m','b','b','b','b','b','b','c','b','b','b','b','b','c','b','b','b','b','b','m'],
            ['m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m','m']]
    if niv == 1 :
        return tab1
    if niv == 2:
        return tab2



def write_file_record(record,name):
    json_string = [{ 'name': name, 'record' : record }]
    json_objects = None
    if not os.path.isfile('result.json'):
        f = open('result.json','a+')
        json_string.append({ 'name': name, 'record' : record })
        json_objects=json.dumps(json_string, indent =2)
        f.write(json_objects)
        f.close()

    else:
        print ('JSON EXIST')
        with open('result.json') as jsonfile:
            json_objects = json.loads(jsonfile.read())

            json_objects.append(json_string)
            #jsonfile.seek(0)
            #json.dump(existingjson, jsonfile)
        print(json_objects)
        jsonfile.close()


    newrecords=json2html.convert(json = json_objects)

    if os.path.isfile('result.html'):
        # Remove l'ancien fichier html
        os.remove("result.html")

    newhtml = open('result.html','a+')
    newhtml.write(newrecords)
    newhtml.close()

    


######################################################################
######################################################################
######################################################################
###### INIT du programme pygame
######################################################################
######################################################################


######################################################################
### Initialisation des deux tableaux pour les deux niveaux.

pygame.init()### Init pygame pour l'initalisation des variables pygame.

tab=init_niveau(1) ### Initialisation du tableau

font = pygame.font.SysFont(None, 25)### Initier la Font systeme utilisé pour le message de la page record.

largeur = len(tab[0])*64 ### Definir la largeur de la page
hauteur = len(tab)*64  ### Définit la hauteur de la page
fenetre = pygame.display.set_mode((largeur, hauteur))       #Ouverture de la fenêtre Pygame
fond = pygame.image.load("fond.png").convert_alpha()        #Chargement et collage du fond
pygame.display.set_caption('Enigma')
Icon = pygame.image.load('kdo3.png')
pygame.display.set_icon(Icon)      
fenetre.blit(fond, (0,0))                                   # position du fond en (x,y) =(0,0)
pygame.display.flip()                                       #actualisation ecran
start, end = 0, 0                                           #definit le temps de début et de fin de la partie
user_text = ''

clock = pygame.time.Clock()                                 #Définit un object clock opour les tick FPS et eviter les lags
fenetre.blit(fond, (0,0))                                   #Définit une page de fond suivant l'image fond prédefinit
all_groups = pygame.sprite.Group()                          #Crée un groupe de Sprite pour la balle et sumuler aussi des collisions
start, velocity, direction = (200, 100), 3, (random.random(), random.random()) # Définit la position de démarrage, la rapidité de la balle, et sa direction aléatoire 
ball = Ball(start, velocity, direction)                     # Instance de la classe Ball pour définir une balle
all_groups.add(ball)                                        # Ajouter l'objet balle héritant de Sprite.

collectCoffre =set_coffrecollection(tab)                    # Récupère la collection d'objet coffre heritant de sprite
nb_coffre =count_coffre(collectCoffre)  
start = time.time()

write_file_record(start,"test")                    # Récupère le nobre d'objet coffre
print(nb_coffre)

############################## 
############################## 
########## BOUCLE INFINE du jeu
run = True
while run:
    coffrevide=None
    clock.tick(60)
    if nb_coffre <= 0:
        end = time.time()
        record_page(start,time.time())
        print ("canceled")
        tab=init_niveau(1)
        fenetre.blit(fond, (0,0))
        all_groups.update()
        print (tab)
        collectCoffre=set_coffrecollection(tab)
        nb_coffre =count_coffre(collectCoffre)
        start = time.time()

        print(nb_coffre)
        
    
    #Re-collage du fond afin d effacer l ancienne position des objets
    fenetre.blit(fond, (0,0))
    all_groups.update()
    # On attrape un event key. 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        # On attrape un event key DOWN (touché préssée) puis on execute les actions d'orientartion de la ballse
        # en fonction de la touche.
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_LEFT:
                ball.moveleft()
            if event.key == pygame.K_RIGHT:
                ball.moveright()
            if event.key == pygame.K_UP:
                ball.moveup()
            if event.key == pygame.K_DOWN:
                ball.movedown()
            if event.key == pygame.K_F1:
                nb_coffre = 0
                fenetre.blit(fond, (0,0))
                all_groups.update()
                collectCoffre=set_coffrecollection(init_niveau(1))
                nb_coffre =count_coffre(collectCoffre)
                tab=init_niveau(1)
            if event.key == pygame.K_F2:
                nb_coffre = 0
                fenetre.blit(fond, (0,0))
                all_groups.update()
                collectCoffre=set_coffrecollection(init_niveau(2))
                nb_coffre =count_coffre(collectCoffre)
                print(nb_coffre)
                tab=init_niveau(2)
    
    # Reflection de la balle contre les parois des murs.
    if ball.rect.left <= 64:
        ball.reflect((1, 0))
    if ball.rect.right >= (largeur-64):
        ball.reflect((-1, 0))
    if ball.rect.top <= 64:
        ball.reflect((0, 1))
    if ball.rect.bottom >= (hauteur-64):
        ball.reflect((0, -1))

    # On charge les images que l'on affichera pour définir l'aire de jeu.
    # L'état de l'air de jeu peut évoluer (ex. collision coffre avec balle donnat un coffre vide)
    imgmur = pygame.image.load("mur.png").convert_alpha()      #Mise en place d'un perso
    imgcoffre = pygame.image.load("coffre.png").convert_alpha() # afficher le coffre dans l'ecran
    imgcoffrevide = pygame.image.load("coffreVide.png").convert_alpha() # afficher le coffre dans l'ecran
    
    # Ici un test de collision de la balle au coffre préinitialisé.
    for i in range(0,len(collectCoffre)):
        rect=imgcoffre.get_rect()
        if ball.rect.colliderect(collectCoffre[i]):
            # Est ce que le coffre etait déjà vide? Sinon on décompte
            if tab[collectCoffre[i].tabi][collectCoffre[i].tabj] != 'v':
                nb_coffre -= 1 
            tab[collectCoffre[i].tabi][collectCoffre[i].tabj] = 'v'
            coffrevide=collectCoffre[i]
            ball.reflect(ball.dir)

    # On insére les murs et coffres férmés ou vides.
    for i in range(0,len(tab)) :
        for j in range(0,len(tab[0])) :
            if tab [i][j]=='m' :
                fenetre.blit(imgmur,(j*64,i*64))
            if tab [i][j] =='c' :
                rect=imgcoffre.get_rect(center=(round(j*64),round(i*64)))
                fenetre.blit(imgcoffre,rect)
            if tab [i][j] =='v' :
                rect=imgcoffrevide.get_rect(center=(round(j*64),round(i*64)))
                fenetre.blit(imgcoffrevide,rect)

    all_groups.draw(fenetre)

    pygame.display.flip()