#!/usr/bin/python

import sys


def help():
    print("Usage: "+sys.argv[0]+" <moltiplicando> <moltiplicatore>")


if len(sys.argv) < 2:
    help()
    exit(0)

print("il risultato di " + sys.argv[1] + "x" +
      sys.argv[2] + " è: " + str(int(sys.argv[1])*int(sys.argv[2])))
