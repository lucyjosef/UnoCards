from Carte import Carte


class CarteUno(Carte):

    def __init__(self, val, coul):
        Carte.valeurs = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Inversion", "Stop", "+2", "+4", "Switch")
        Carte.couleurs = ("Rouge", "Vert", "Bleu", "Jaune", "Joker")
        super().__init__(val, coul)

    @staticmethod
    def validation(val, coul):
        if val < 0 or val > 14:
            raise Exception("La valeur d'une carte est comprise entre 0 et 14")
        if coul < 0 or coul > 4:
            raise Exception("Le code couleur d'une carte est compris ente 0 et 3")

    def __str__(self):
        return str(Carte.valeurs[self.valeur]) + "(" + Carte.couleurs[self.couleur] + ")"

    def __eq__(self, other: Carte):
        if self.valeur == other.valeur \
            or self.couleur == other.couleur \
                or self.couleur == (len(Carte.couleurs) - 1):
                    return True
        else:
            return False
