#!/usr/bin/python3


# COUNTSYL.FNC

# DPL

# This function can be used to count the number of syllables.

import sys
import re

def StripStressMarkers(String):

    with open(dpw.cd,'r') as wordfile:
        for word in wordfile:
            re.sub("'","",String)
    return(String)


def CountSyllables(String):

    if (String == ""):
        return(0)
    else:
        return(re.sub(/-/,"",String) + 1)

def main(argv): 

    word = str(sys.argv[1])

    print(CountSyllables(StripStressMarkers($4))


main(sys.argv[1])
