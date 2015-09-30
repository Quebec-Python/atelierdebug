

def estPremier(a):
    """Retourne True si `a` est un nombre premier."""
    return all(a % i for i in range(2, a))


def nombresNonPremiers(n):
    """Retourne des nombres pairs jusqu'a `n`."""
    # Generer tous les nombres jusqu'a n
    out = list(range(1, n + 1))

    # Enlever les nombres premiers
    for i in range(len(out)):
        if estPremier(out[i]):
            del out[i]

    return out


if __name__ == '__main__':
    print(nombresNonPremiers(20)) # Devrait afficher [1, 4, 6, 8, 9]
