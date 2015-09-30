


def conditionalPrint(cond, val):
    """Affiche `val` si `cond` est FAUX."""
    if cond == False:
        print(val)


if __name__ == '__main__':
    conditionalPrint(1 == 0, "Bonjour!") # Devrait afficher
    conditionalPrint(2 in [1, 2, 3], "Le monde!") # Ne devrait pas afficher
    conditionalPrint(5 - 10/2, "Erreur?") # Ne devrait pas afficher
