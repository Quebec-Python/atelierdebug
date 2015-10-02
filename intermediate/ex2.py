

def myFunction(iterableToCheck, allowedRepetitions=2, initSeenItems={}):
    """
    Vérifie que l'itérable iterableToCheck ne contient pas plus de
    'allowedRepetitions' occurrences de chaque élément unique. Retourne True
    si c'est le cas, et False sinon. Par exemple, si allowedRepetitions=2,
    l'itérable [1, 3, 5, 5, 8, 9] est valide, mais pas [1, 2, 2, 2, 5, 6, 7].

    L'utilisateur peut également fournir un dictionnaire pour initialiser
    l'algorithme. Dans ce cas, les couples (item, count) du dictionnaire
    sont utilisés comme valeurs initiales pour chaque item de iterableToCheck.
    
    Par exemple, si allowedRepetitions=2 et que initSeenItems={4:2}, alors
    iterableToCheck ne peut contenir AUCUN 4.
    """

    # On initialise le dictionnaire d'éléments déjà vu avec celui
    # fourni par l'utilisateur (vide par défaut)
    seenItems = initSeenItems

    for v in iterableToCheck:
        # Pour chaque élément de iterableToCheck, s'il n'est pas déjà présent
        # dans notre dictionnaire, on l'ajoute, sinon on incrémente son compteur
        if v not in seenItems:
            seenItems[v] = 1
        else:
            seenItems[v] += 1

        # Si on a vu cet élément trop souvent
        if seenItems[v] > allowedRepetitions:
            return False
    # Pas d'erreur (puisqu'on est sorti de la boucle normalement)
    return True



if __name__ == '__main__':
    it1 = [1, 3, 5, 5, 8, 9]
    print("Check iterable {} : {}".format(it1, myFunction(it1)))    # Devrait être True

    it2 = [1, 2, 2, 2, 5, 6, 7]
    print("Check iterable {} : {}".format(it2, myFunction(it2)))    # Devrait être False
    print("Check iterable {} : {}".format(it2, myFunction(it2, allowedRepetitions=3)))  # Devrait être True

