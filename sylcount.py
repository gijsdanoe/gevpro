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

def word():
    with open("dpw.cd",'r') as wordfile:
        for line in wordfile:
            word = re.search(r'\\(.*?)\\', line)
        return word.group(1)

def CountSyllables(String):

    stressmarkcount = 0
    syllables = re.search(r'\\(.*?\\', String)
    word = syllables.group(2)
    for line in String:
        for char in word:
            if char == "-":
                stressmarkcount += 1
    return stressmarkcount + 1


def main(): 

    mydict = {}
    mydict[word()] = CountSyllables(String)
    print(mydict)


if __name__ == "__main__":
    main()
