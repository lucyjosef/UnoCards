from JeuCartes import JeuCartes


class Paquet(JeuCartes):

    def __init__(self):
        super().__init__(True)

    def ajouter(self, carte):
        self.cartes.append(carte)
