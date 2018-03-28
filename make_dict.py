import pickle

def main():
    dicto = {}
    with open("dpw.cd", "r") as wordfile:
        for line in wordfile:
             words = []
             line = r"{0}".format(line)
             words = line.split("\\")
             dicto[words[1]] = words[3]
    pickle.dump(dicto, open("dpw.p", "wb"))

main()

