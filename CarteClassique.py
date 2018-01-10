from Carte import Carte


class CarteClassique(Carte):

    def __init__(self, val, coul):
        Carte.valeurs = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As")
        Carte.couleurs = ("Coeur", "Carreau", "Trèfle", "Pique")
        super().__init__(val, coul)

    @staticmethod
    def validation(val, coul):
        if val < 2 or val > 14:
            raise Exception("La valeur d'une carte est comprise entre 2 et 14")
        if coul < 0 or coul > 3:
            raise Exception("Le code couleur d'une carte est compris ente 0 et 3")

