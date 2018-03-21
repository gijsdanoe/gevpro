#!/usr/bin/python3


# COUNTSYL.FNC

# DPL

# This function can be used to count the number of syllables.

import sys
import re



def word():
    with open("dpw.cd",'r') as wordfile:
        for line in wordfile:
            word = re.findall(r'\\(.*?)\\', line)
        return word.group(1)

def CountSyllables():
    with open("dpw.cd",'r') as wordfile:
        for line in wordfile:
            wd = re.findall(r'my_regex', line, re.IGNORECASE)
            stressmarkcount = 0
            for char in line:
                if char == "-":
                     stressmarkcount += 1
            word = re.findall(r'\\(.*?)\\', line).group(1)
    for char in word:
        if char == "-":
            return stressmarkcount
        else:
            return stressmarkcount + 1


def main():
    global my_regex
    my_regex = re.escape(sys.argv[1])
    with open("dpw.cd", 'r') as wordfile:
        for line in wordfile:
            wd = re.findall(r'my_regex', line, re.IGNORECASE)

    print(wd)


if __name__ == "__main__":
    main()
