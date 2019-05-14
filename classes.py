"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import *
from constantes import *
from random import *

class Niveau:
    """Classe permettant de créer un niveau"""
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

        def generer(self):
            """Méthode permettant de générer le niveau en fonction du fichier.
            On crée une liste générale, contenant une liste par ligne à afficher"""
            #On ouvre le fichier
            with open(self.fichier, "r") as fichier:
                structure_niveau = []
                #On parcourt les lignes du fichier
                for ligne in fichier:
                    ligne_niveau = []
                    #On parcourt les sprites (lettres) contenus dans le fichier
                    for sprite in ligne:
                        #On ignore les "\n" de fin de ligne
                        if sprite != '\n':
                            #On ajoute le sprite à la liste de la ligne
                            ligne_niveau.append(sprite)
                            #On ajoute la ligne à la liste du niveau
                            structure_niveau.append(ligne_niveau)
                            #On sauvegarde cette structure
                            self.structure = structure_niveau


    def afficher(self, fenetre):
        """Méthode permettant d'afficher le niveau en fonction
        de la liste de structure renvoyée par generer()"""
        #Chargement des images (seule celle d'arrivée contient de la transparence)
        mur = pygame.image.load(image_mur).convert()
        depart = pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()

        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':		   #m = Mur
                    fenetre.blit(mur, (x,y))
                elif sprite == 'd':		   #d = Départ
                        fenetre.blit(depart, (x,y))
                elif sprite == 'a':		   #a = Arrivée
                            fenetre.blit(arrivee, (x,y))
                            num_case += 1
                            num_ligne += 1


class Perso:
    """Classe permettant de créer un personnage"""
    def __init__(self, image, niveau):
        #Sprites du personnage
        self.image = pygame.image.load(image).convert_alpha()
        #Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #Direction par défaut
        self.direction = self.image
        #Niveau dans lequel le personnage se trouve
        self.niveau = niveau
        self.compteur = 0


        def deplacer(self, direction):
            """Methode permettant de déplacer le personnage"""
            if (self.niveau.structure[self.case_y][self.case_x] == 'i'):
                self.compteur += 1
                print(self.compteur)
                self.niveau.structure[self.case_y][self.case_x] = '0'
                #Déplacement vers la droite
                if direction == 'droite':
                    #Pour ne pas dépasser l'écran
                    if self.case_x < (nombre_sprite_cote - 1):
                        #On vérifie que la case de destination n'est pas un mur
                        if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                            #Déplacement d'une case
                            self.case_x += 1
                            #Calcul de la position "réelle" en pixel
                            self.x = self.case_x * taille_sprite
                            #Image dans la bonne direction
                            self.direction = self.image

                            #Déplacement vers la gauche
                            if direction == 'gauche':
                                if self.case_x > 0:
                                    if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                                        self.case_x -= 1
                                        self.x = self.case_x * taille_sprite
                                        self.direction = self.image

    #Déplacement vers le haut
    if direction == 'haut':
        if self.case_y > 0:
            if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                self.case_y -= 1
                self.y = self.case_y * taille_sprite
                self.direction = self.image

    #Déplacement vers le bas
    if direction == 'bas':
        if self.case_y < (nombre_sprite_cote - 1):
            if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                self.case_y += 1
                self.y = self.case_y * taille_sprite
                self.direction = self.image


class Item:
    """Classe permettant de créer un personnage"""

    def __init__(self, image, niveau):
        # Sprites de l'objet
        self.image = pygame.image.load(image).convert_alpha()
        # Niveau dans lequel l'objet se trouve
        self.niveau = niveau
        self.case_x = 0
        self.case_y = 0

    continuer = True
    while continuer:
        x = randint(0,14)
        y = randint(0,14)
        if self.niveau.structure[y][x] == '0':
            continuer = False
            self.niveau.structure[y][x] = 'i'
            else:
                continuer = True

    # Position de l'objet en cases et en pixels
    self.case_x = x
    self.case_y = y
    self.x = self.case_x * 30
    self.y = self.case_y * 30
    print(self.niveau.structure)

