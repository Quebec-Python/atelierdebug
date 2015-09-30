

def compareLists(list1, list2):
    """
    Compare deux listes sans tenir compte de la position respective de leurs
    éléments. Par exemple, [1, 2, 3, 4] et [3, 1, 2, 4] sont considérées
    égales, mais [1, 2, 3, 4] et [4, 3, 2, 5] ne le sont pas.
    """
    
    # Premier test, on vérifie si les deux listes ont la même longueur
    if len(list1) != len(list2):
        return False
    
    # Si les longueurs sont égales, alors on trie les listes
    # pour assurer qu'on compare les mêmes éléments.
    list1 = list1.sort()
    list2 = list2.sort()
    
    # On peut alors utiliser directement la comparaison de liste de Python
    # (puisque les éléments sont ordonnés)
    return list1 == list2



if __name__ == '__main__':
    l1 = [1, 2, 3, 4]
    l2 = [4, 3, 1, 2]
    print("Est-ce que {} et {} sont égales? {}".format(l1, l2, compareLists(l1, l2)))   # Devrait être vrai
    
    l3 = [5, 6, 7, 8]
    l4 = [6, 7, 8]
    print("Est-ce que {} et {} sont égales? {}".format(l3, l4, compareLists(l3, l4)))   # Devrait être faux
    
    l5 = [1, 2, 3, 4]
    l6 = [4, 3, 5, 1]
    print("Est-ce que {} et {} sont égales? {}".format(l5, l6, compareLists(l5, l6)))   # Devrait être faux
