from Carte import Carte
from random import shuffle


class JeuCartes:

    def __init__(self, vide=False):
        if self.__class__ is JeuCartes:
            raise Exception("Construction directe interdite!")
        else:
            self.__cartes = []
            if not vide:
                self.initialiser()

    def initialiser(self):
        pass

    def __str__(self):
        jeu_cartes = ""
        for carte in self.__cartes:
            if jeu_cartes == "":
                jeu_cartes = str(carte)
            else:
                jeu_cartes += ", " + str(carte)

        return jeu_cartes

    def melanger(self):
        shuffle(self.__cartes)

    def tirer(self):
        try:
            return self.__cartes.pop(0)
        except IndexError:
            print("Il n'y a plus de carte")
            raise IndexError
            return None

    def __getCartes(self):
        return self.__cartes

    def __setCartes(self, carte):
        if len(self.__cartes) > 52:
            raise Exception("Jeu complet")
        self.__cartes.append(carte)

    cartes = property(__getCartes, __setCartes)

    def __add__(self, carte):
        print("__ADD__ surcharge d'opérateur")
        self.ajouter(carte)

    def __len__(self):
        return len(self.__cartes)
