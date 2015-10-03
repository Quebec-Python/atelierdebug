'''
@author: Dépanneurs GLO-1901 2013h

Module principal du TP6
'''

__auteur__ = "idul"
__date__ = ""
__coequipiers__ = ""

from jeu import Jeu
from joueur import JoueurHumain, JoueurOrdinateur
import argparse


def parserArguments():
    '''Parse les arguments de la ligne de commande.'''
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n",
                        type=int,
                        default=8,
                        help="nombre de rangées")
    parser.add_argument("--kmin",
                        type=int,
                        default=4,
                        help="quantité minimale d'allumettes par rangée")
    parser.add_argument("--kmax",
                        type=int,
                        default=30,
                        help="quantité maximale d'allumettes par rangée")
    parser.add_argument("--humains",
                        type=int,
                        default=1,
                        choices=range(3),
                        help="nombre de joueurs humains")
    return parser.parse_args()


def main():
    '''Fonction principale du jeu de Nim.'''
    args = parserArguments()
    jeu = Jeu(args.n, args.kmin, args.kmax)
    
    # créer les deux joueurs
    joueurs = []
    # créer les joueurs humains
    for num in range(args.humains):
        defaut = "HUMAIN-{}".format(num+1)
        nom = input("Entrez le nom du joueur {} (défaut={}) >>> ".format(num+1, defaut))
        if nom == '': nom = defaut
        joueurs.append(JoueurHumain(nom))
    # créer les joueurs ordinateurs
    for num in range(2 - args.humains):
        joueurs.append(JoueurOrdinateur("ORDI-{}".format(num+1)))

    # jouer la partie avec les deux joueurs
    jeu.jouerPartie(*joueurs)

if __name__ == '__main__':
    main()