from JeuCartes import JeuCartes
from CarteUno import CarteUno


class JeuCartesUno(JeuCartes):

    def initialiser(self):
        for val in range(13):
           for coul in range(4):
               self.cartes.append(CarteUno(val, coul))

        for val in range(13, 15):
            for i in range(4):
                self.cartes.append(CarteUno(val, 4))
