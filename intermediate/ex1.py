

def myFunction(dictSource, dictTest, tol=0.2):
    """
    Pour chaque clé dans dictSource (un dictionnaire), cette fonction teste
    si la même clé dans dictTest contient la même valeur, avec une tolerance
    de tol.
    Retourne une liste contenant les clés qui ne sont pas égales (en tenant
    compte de la tolérance demandée), ou une liste vide si toutes les clés
    sont équivalentes.

    Si une clé est présente dans dictSource mais pas dans dictTest, elle est
    ignorée et n'empêche pas la fonction de retouner une liste.
    """
    retList = []
    for key, val in dictSource.items():
        # On parcours le dictionnaire source
        try:
            if not val-tol < dictTest[key] < val + tol:
                # Si on est en dehors de la tolérance,
                # on ajoute la paire de valeurs incorrectes à notre liste
                retList.append(val, dictTest[key])
        except:
            # Si dictTest[key] génère une KeyError, ce n'est pas grave,
            # puisque la fonction peut dans ce cas simplement ignorer le cas
            # et considérer la comparaison réussie.
            # On n'a qu'à passer à la clé suivante
            pass
    return retList


if __name__ == '__main__':
    d1 = {'a' : 25, 'b' : 41.5, 'c' : 88.1}
    d2 = {'b' : 41.55, 'c' : 88, 'd' : 15}
    print("Comparing {} and {} : {}".format(d1, d2, myFunction(d1, d2)))
    # Devrait être : []


    d3 = {'b' : 41.5, 'c' : 88.1, 'a' : 25}
    d4 = {'b' : 1e10, 'c' : 88, 'd' : 15}
    print("Comparing {} and {} : {}".format(d3, d4, myFunction(d3, d4)))
    # Devrait être [(41.5, 1e10)]
