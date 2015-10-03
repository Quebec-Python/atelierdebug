#!/usr/bin/env python

from hypothesis import given
from hypothesis.strategies import text


# Les fonctions a tester. Exemples d'emploi:
# encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
# decode([('a', 5), ('h', 6), ('m', 7), ('u', 1), ('i', 7), ('a', 6)])

def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q


# Test d'Hypothesis

@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s


if __name__ == '__main__':
    test_decode_inverts_encode()
