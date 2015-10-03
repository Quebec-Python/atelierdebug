

def numericDict(list):
    """Cree un dictionnaire"""
    # Cree
    v = list

    # Cree la liste des clefs
    k = list(range(len(v)))

    # Genere un dictionnaire avec les clefs et les valeurs
    return dict(zip(k, v))


if __name__ == '__main__':
    res = numericDict(['a', 'b', 'c']) # Devrait retourner {0: 'a', 1: 'b', 2: 'c'}
