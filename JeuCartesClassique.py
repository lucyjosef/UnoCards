from JeuCartes import JeuCartes
from CarteClassique import CarteClassique


class JeuCartesClassique(JeuCartes):

    def initialiser(self):
        for val in range(2, 15):
           for coul in range(4):
               self.cartes.append(CarteClassique(val, coul))
