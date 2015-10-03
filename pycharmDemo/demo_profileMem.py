__author__ = 'Marc-Andre Gardner'

import numpy as np

@profile
def myFunction(s):
    a1 = np.ones((s, s**2), dtype=np.float64)
    a2 = np.zeros((s, s+1, s+2), dtype=np.int8)
    a3 = np.empty((s**2/8, s**2/16), dtype=np.uint32)
    l1 = [8]*s**2
    d1 = {k:1.2 for k in range(s*20)}

    #a3[:] = 0
    #a2[:] = 12

    return s


if __name__ == '__main__':
    myFunction(500)