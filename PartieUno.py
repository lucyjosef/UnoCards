from Paquet import Paquet
from JeuCartesUno import JeuCartesUno
from CarteUno import CarteUno

class PartieUno:

    def __init__(self, *args):
        self.__jeu = JeuCartesUno()
        self.__pile = Paquet()
        self.__joueurs = []
        self.__participant = args
        self.direction = 1
        self.tour = 0
        self.old = False

        for joueur in args:
            self.__joueurs.append(joueur)

    def demarrerPartie(self):
        self.__melanger()
        self.__distribuer()

        self.__pile.ajouter(self.__jeu.tirer())

        poursuivre = True
        while poursuivre:
            print("Direction du jeu " + self.__direction())
            print("Carte sur la pile " + str(self.__pile.cartes[0]))
            if not self.old:
                self.old = self.__readCarte()

            joueur = self.__joueurs[self.tour]
            poursuivre = self.__main(joueur)
            if len(joueur.paquet) == 0:
                print(str(joueur) + " gagnant")
                joueur.victoire += 1
                self.__joueurs.pop(self.tour)
            self.__nextJoueur()
            print("==== TOUR SUIVANT ====")

    def __distribuer(self):
        for i in range(3):
            for joueur in self.__joueurs:
                joueur.ajouter(self.__jeu.tirer())

    def __main(self, joueur):
        print("Au tour de : " + str(joueur))
        print("Carte en main (" + str(len(joueur.paquet)) + ") : " + str(joueur.paquet))
        flag = False
        while not flag:
            x = input("Choisir une carte (x pour piocher) : ")
            if x == "x":
                flag = True
            elif int(x) < 0 or int(x) > len(joueur.paquet) - 1:
                print("Veuillez choisir une carte de votre main")
            elif joueur.paquet.cartes[int(x)] == self.__pile.cartes[0]:
                flag = True
            else:
                print("Carte incorrect, veuillez choisir même couleur ou même valeur ou Joker")

        if x == "x":
            joueur.ajouter(self.__jeu.tirer())
        else:
            self.__pile.cartes.insert(0, joueur.paquet.cartes.pop(int(x)))
            self.old = False

        return True

    def __melanger(self):
        self.__jeu.melanger()

    def __readCarte(self):
        val = self.__pile.cartes[0].valeur
        if val > 9:
            if val == 10:
                self.__inversion()
            elif val == 11:
                self.__nextJoueur()
            elif val == 12:
                self.__addCartes(2)
                self.__nextJoueur()
            elif val == 13:
                self.__addCartes(4)
                self.__switch()
                self.__nextJoueur()
            elif val == 14:
                self.__switch()
        return True

    def __inversion(self):
        self.direction = self.direction * -1
        print("Changement de direction vers la " + self.__direction())

    def __direction(self):
        if self.direction == 1:
            return "Droite"
        else:
            return "Gauche"

    def __nextJoueur(self):
        self.tour = (self.tour + self.direction) % len(self.__joueurs)

    def __addCartes(self, nbr):
        for i in range(nbr):
            self.__joueurs[self.tour].ajouter(self.__jeu.tirer())

    def __switch(self):
        flag = False
        while not flag:
            coul = int(input("Veuillez choisir une couleur entre (0) Rouge, (1) Vert, (2) Bleu, (3) Jaune : "))
            if coul < 0 or coul > 4:
                print("Le code couleur d'une carte est compris ente 0 et 3")
            else:
                flag = True
        print("Couleur choisie : " + CarteUno.couleurs[coul])
        self.__pile.cartes[0].couleur = coul
