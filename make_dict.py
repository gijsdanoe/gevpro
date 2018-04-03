import pickle

def count_syl(words):
    """Counts the syllables of a tweet."""
    syl_count = 0
    for item in words:
        if item in ".!?,:;#()@/0123456789":
            syl_count += 0
        else:
            syl_count = syl_count + (words[3].count("-") + 1)
    return syl_count

def main():
    dicto = {}
    with open("dpw.cd", "r") as wordfile:
        for line in wordfile:
             line = line.lower()
             words = []
             line = r"{0}".format(line)
             words = line.split("\\")
             dicto[words[1]] = count_syl(words)
    pickle.dump(dicto, open("dpw.p", "wb"))

main()

