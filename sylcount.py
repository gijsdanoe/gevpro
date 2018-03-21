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
    for line in String:
        for char in line:
            if char == "-":
                stressmarkcount += 1
    with open("dpw.cd",'r') as wordfile:
        for line in wordfile:
            word = re.search(r'\\(.*?)\\', line).group(1)
    for char in word:
        if char == "-":
            return stressmarkcount
        else:
            return stressmarkcount + 1


def main(): 
    String = StripStressMarkers()
    mydict = {}
    mydict[word()] = CountSyllables(String)
    print(mydict)


if __name__ == "__main__":
    main()
