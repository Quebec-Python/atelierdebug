

def computeMeanValues(seq, timesAdd=1):
    """
    Reçoit une séquence de sous-séquences, par exemple [[1, 2, 3], [6, 5, 1]].
    Pour chacune des sous-séquences, calcule la moyenne de la sous-séquence,
    puis l'ajoute 'timesAdd' fois à la sous-séquence, in place. Par exemple,
    avec l'argument [[1, 2, 3], [6, 5, 1]], le résultat (la valeur de seq
    modifiée par référence), le résultat doit être [[1, 2, 3, 2], [6, 5, 1, 4]]

    Par ailleurs, la fonction doit retourner un tuple contenant 4 éléments :
    - Le nombre de sous-séquences non vides
    - La somme des longueurs des sous-séquences
    - Une liste contenant la moyenne de chaque sous-séquence
    - Un booléen indiquant si la modification par référence a fonctionné ou non
        (voir paragraphe suivant)
    
    Il se peut que la séquence principale soit immuable, par exemple par c'est
    un tuple. Dans ce cas, la fonction ne doit pas modifier l'élément par
    référence (puisque c'est impossible), et seulement retourner le tuple de
    4 éléments mentionné plus haut, sans lancer d'exception.
    """
    listMeans = []
    nNonEmpty = 0
    totalSum = 0
    succeed = True
    for subseqIdx in range(len(seq)):
        s, n = sum(seq[subseqIdx]), len(seq[subseqIdx])
        if n == 0:
            # Si on a un itérable vide, on passe au suivant
            # pour éviter une division par zéro (notons que dans tous les cas,
            # les valeurs de totalSum et nNonEmpty seront correctes)
            continue
        mean = s / n
        listMeans.append(mean)
        totalSum += s
        nNonEmpty += n > 0
        try:
            seq[subseqIdx] += [mean] * timesAdd
        except TypeError:
            # Ok, la séquence ne peut être modifiée (c'est un tuple par exemple)
            # On ignore l'erreur, mais en le signalant
            succeed = False
            continue
    return nNonEmpty, totalSum, listMeans, succeed


def myFunction(tuple1, tuple2):
    """
    Reçoit deux tuples contenant chacun un nombre arbitraire de listes (avec
    le même nombre de listes pour les deux tuples).
    """
    # Même si on sait que le fait qu'on reçoive des tuples en argument empêche
    # computeMeanValues de les modifier par référence, on peut quand
    # même utiliser la fonction pour obtenir les statistiques sur ces séquences
    statsSeq1 = computeMeanValues(tuple1)
    statsSeq2 = computeMeanValues(tuple2)

    # On s'assure que les tuples ont bien été intouchés en vérifiant que
    # leur modification a levé un TypeError, indiqué par le dernier élément
    # du tuple retourné par computeMeanValues
    assert statsSeq1[3] == False and statsSeq2[3] == False, "Erreur! Tuples modifiés!"

    import pdb; pdb.set_trace()



if __name__ == '__main__':
    myFunction(([1,2,3], [0, 1]), 
                ([4,4,8,10], [2,5,8]))

