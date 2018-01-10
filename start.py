from Joueur import Joueur
from PartieUno import PartieUno

if __name__ == "__main__":
    j1 = Joueur("Duck", "Donald")
    j2 = Joueur("Duck", "Daisy")
    j3 = Joueur("Duck", "Picsou")

    p = PartieUno(j1, j2, j3)
    p.demarrerPartie()





