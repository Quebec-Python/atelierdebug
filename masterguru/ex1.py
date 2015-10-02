#!/usr/bin/env python

# Etant donne ce code:
code = """
g = 5
x = [g for i in range(5)]
"""


# Ceci fonctionne:
exec(code)
# (Cleanup)
del g, x


# Pourquoi est-ce que ceci ne fonctionne pas?
def f(code_str):
    exec(code_str)

f(code) 
