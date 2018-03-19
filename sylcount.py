#!/usr/bin/python3


# COUNTSYL.FNC

# DPL

# This function can be used to count the number of syllables.

import sys
import re

def StripStressMarkers():

    with open("dpw.cd",'r') as wordfile:
        for line in wordfile:
            String = line.replace("'", "")
    return String


def CountSyllables(String):

    stressmarkcount = 0
    for line in String:
        for char in line:
            if char == "-":
                stressmarkcount += 1
    return stressmarkcount + 1

def main(): 
    String = StripStressMarkers()
    print(CountSyllables(String))


if __name__ == "__main__":
    main()
