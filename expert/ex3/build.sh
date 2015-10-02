#!/bin/bash
gcc -shared -Wl,-soname,adder -g -o adder.so -fPIC add.c
