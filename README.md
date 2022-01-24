## Projet Enigma - Cahier des Charges et Instructions

### Objectif du projet

L'objectif de ce projet est de mettre en oeuvre un jeu en 2 niveau se basant sur la librairie python pygame. 

#### Le premier niveau du jeu
Ce premier niveau a pour objectif d'afficher une aire de jeu ayant une taille largeur x hauteur se basant sur un tableau en deux dimensions préinitialisé.
Ce tableau est composé de valeurs indiquant le type de pixel:

* 'm' pour le pixel mur
* 'c' pour le pixel coffre fermé

La balle est inséré au démarrage dans une position libre au developpeur.

A chaque contact de la balle sur les coffres, ces derniers deviennent des coffres vide.


#### Le deuxieme niveau
Ce niveau est libre en terme de développement. 

### Installation
Python 2.6 ou 3.x doit etre installé sur votre système d'exploitation.
Le dossier enigma peut etre installé sur votre système Windows.
Le dossier comprends les compsants suivants:
* Installer les librairies via pip install: pygame, 
* Le fichier source python 
* Les sources d'images (*.png)
* Le présent document d'explication 'Lisez Moi' écrit en language markdown pour etre intégré dans un repertoire communautaire de type github.  

### Guide d'utilisation

La balle rebondit sur les murs et les coffres. L'orientation et la direction de la balle peut etre fait via les touches UP, DOWN, LEFT et RIGHT. Ces touches orientant la balle.

Le joueur doit vider les coffres en les touchant avec la balle. A la fin de chaque partie un temps sera relevé. Vous pouvez saisir votre Nom.

### Guide des touches
* F1 : Pour passer au niveau 1 en cours de jeu
* F2 : Pour passer au niveau 2 en cours de jeu
* ECHAPE : Pour quittert le jeu

A la fin de chaque partie:
* F9 : Pour redemarrer au niveau 1
* ENTREE: Pour valider votre score
* ECHAPE: Pour quitter le jeu

### Resultat des scores
Ces derniers sont stockés en HTML et en json.



### Contacts
Dev: martinezamarimarion@gmail.com
ou le code est disponnible sur le compte github de l'association Lightpharos.io sur:
https://github.com/lightpharosio/enigma
