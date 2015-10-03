'''
@author: Dépanneurs GLO-1901 2013h

Module de joueurs.
Contient une classe générique Joueur de laquelle les classes JoueurHumain et
JoueurOrdinateur sont dérivés.
'''

__auteur__ = "idul"
__date__ = ""
__coequipiers__ = ""

import operator
import random
from functools import reduce


class Joueur:
    '''Classe de base du joueur à dériver.'''
    def __init__(self, nom):
        '''Construire un joueur à partir de son nom.'''
        self.nom = nom

    def __str__(self):
        '''Retourne le nom du joueur.'''
        return self.nom
        
    def choisirCoup(self, jeu):
        '''
        Méthode abstraite à implémenter dans les classes dérivées.
        Doit retourner le coup à effectuer sous la forme d'un tuple (Rangée, Quantité).
        '''
        raise NotImplementedError


class JoueurHumain(Joueur):
    '''
    Encapsule l'interaction avec un joueur humain.
    '''
    def choisirCoup(self, jeu):
        '''Effectue une interaction avec un joueur par la console.
        Retourne l'action désirée par le tuple (Rangée, Quantité)'''
        ok = False
        while not ok:
            coup = input("Quel coup désirez-vous effectuer (q pour quitter)? Séparez la rangée et la "
                         "quantité par un espace. ( e.g.: A 3 )\n>>> ")
            if len(coup.split()) == 1:
                continue
            if not coup.split()[0] in jeu:
                continue
            try:
                i = int(coup.split()[1])
            except ValueError:
                continue
            if i <= 0 or i > jeu[coup.split()[0]]:
                continue
            if coup == 'q':
                raise KeyboardInterrupt
            ok = True

        return coup.upper().split()


class JoueurOrdinateur(Joueur):
    '''
    Encapsule un joueur artificiel.
    '''
    def choisirCoup(self, jeu):
        '''
        Implante l'algorithme du syndrome.
        Retourne un tuple (rangee, quantité) contenant le nom de la rangée
        à choisir ainsi que le nombre d'allumettes à retirer.
        '''
        # calculer le syndrome
        syndrome = reduce(operator.xor, jeu.values())
        # effectuer le calcul pour annuler le syndrome
        coups = map(lambda nom: (nom, jeu[nom]-(jeu[nom]^syndrome)), jeu)
        # construire la liste des coups gagnants
        gagnants = sorted(filter(lambda coup: coup[1] > 0, coups))
        if gagnants:
            # retourner un des coups gagnants
            print("Les coups gagnants sont:")
            for coup in gagnants:
                print(coup[0], coup[1])
            return random.choice(gagnants)
        else:
            # aucun coup n'est gagnant; retirer une allumette dans une des rangées
            return random.choice(list((nom, 1) for nom in jeu if jeu[nom] > 0))
