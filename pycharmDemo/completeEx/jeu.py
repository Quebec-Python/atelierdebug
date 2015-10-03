'''
@author: Dépanneurs GLO-1901 2013h

Module du jeu des allumettes (jeu de Nim)
'''

__auteur__ = "idul"
__date__ = ""
__coequipiers__ = ""

from random import randint
import itertools
import string


class Jeu(dict):
    '''
    Classe du jeu des allumettes (jeu de Nim). Encapsule l'état interne du jeu
    et permet d'interagir avec celui-ci.
    '''
    def __init__(self, n, kmin, kmax):
        '''
        Constructeur du jeu de Nim. Crée une quantité de rangée *n* 
        contenant toutes une quantité d'allumettes entre *kmin* et *kmax*.  
        '''
        assert n > 0, "Vous devez fournir une quantité de rangée entière strictement positive"
        assert kmin > 0, ("Vous devez fournir une quantité minimale d'allumettes entière "
                          "strictement positive")
        assert kmax > 0, ("Vous devez fournir une quantité maximale d'allumettes entière "
                          "strictement positive")

        alphabet = string.ascii_uppercase 

        valeurs = dict(
            [(alphabet[index], randint(kmin, kmax)) for index in range(n)]
        )
        super().__init__(valeurs)

    def __str__(self):
        '''
        Retourne l'affichage du jeu.
        '''
        entete = list(range(0, max(self.values()) + 11, 10)) 
        result = "\t{entete_format}\n".format(
            entete_format="".join(
                ["{:<10}".format(i) for i in entete]
            ),
        )
        result += "Col.\t+{entete_format}+\n".format(
            entete_format="+".join([("=" * 9) for _ in entete[:-1]]),                                             
        )
        for rang, qte in sorted(self.items()):
            result += "{rang} ({qte})\t {allumettes}\n".format(
                rang=rang,
                qte=qte,
                allumettes='|' * qte,
            )
        return result

    def jouer1Coup(self, joueur):
        '''
        Demande au joueur de choisir son coup avec l'état actuel du jeu.
        '''
        coup = joueur.choisirCoup(self)
        print("{} a joué: {} {}".format(joueur, *coup))
        self.retirer(*coup)

    def jouerPartie(self, joueur1, joueur2):
        '''
        Joue une partie de Nim entre deux joueurs.
        '''
        tour = 0
        for joueur in itertools.cycle((joueur1, joueur2)):
            # afficher l'état du jeu
            tour += 1
            print("\nTour #{}".format(tour))
            print("C'est au tour de {} à jouer...".format(joueur))
            print(self)

            self.jouer1Coup(joueur)
            if self.termine(): break

        print("{} a gagné!".format(joueur))

    def retirer(self, rangee, quantite):
        '''
        Retire *quantite* (nombre) d'allumettes de la rangée *rangee* (texte).
        '''
        self[rangee] -= int(quantite)

    def termine(self):
        '''
        Retourne si le jeu est terminé (True / False)
        '''
        return sum(self.values()) == 0