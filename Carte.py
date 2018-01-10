class Carte:

    valeurs = None
    couleurs = None

    def __init__(self, val,     coul):
        if self.__class__ is Carte:
            raise Exception("Construction directe interdite!")

        self.__class__.validation(val, coul)
        self.__valeur = val
        self.__couleur = coul


    @staticmethod
    def validation():
        pass

    def affiche(self):
        print(Carte.valeurs[self.__valeur], "de", Carte.couleurs[self.__couleur])

    # Affichage Ascii d'une carte
    def affiche_ascii(self):
        nom = str(Carte.valeurs[self.__valeur]) + " de " + Carte.couleurs[self.__couleur]
        taille = len(nom) + 2
        print("/", "-" * taille, "\\", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", nom, "|")
        print("|", " " * taille, "|", sep="")
        print("\\", "-" * taille, "/", sep="")

    def __str__(self):
        return str(Carte.valeurs[self.__valeur]) + " de " + Carte.couleurs[self.__couleur]

    def __getValeur(self):
        return self.__valeur

    def __setValeur(self, val):
        self.__valeur = val

    valeur = property(__getValeur, __setValeur)

    def __getCouleur(self):
        return self.__couleur

    def __setCouleur(self, val):
        self.__couleur = val

    couleur = property(__getCouleur, __setCouleur)
