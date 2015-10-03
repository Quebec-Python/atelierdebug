#!/bin/bash
py-afl-fuzz -t 1000 -o results/ -i examples_images/ -- /usr/bin/python ex_im.py
