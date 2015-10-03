import sys

import afl

from PIL import Image


while afl.loop(100):
    try:
        im = Image.open(sys.stdin.buffer)
        im.load()
    except IOError as e:
        print("IOError: {}".format(e))
