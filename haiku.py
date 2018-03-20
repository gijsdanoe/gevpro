#!/usr/bin/python3

def haiku(tweet, tweetdict):
    sentence1 = [tweet[0]]
    sentence2 = []
    sentence3 = []
    index = 0
    word = tweet[index]
    syltotal = tweetdict[word]
    while True:
        if syltotal < 5:
            index +=1
            word = tweet[index]
            syltotal += tweetdict[word]
            sentence1.append(word)
        elif syltotal == 5:
            sentence1.append(word)
            break
    index +=1
    word = tweet[index]
    syltotal += tweetdict[word]
    while True:
        if syltotal < 12:
            index +=1
            word = tweet[index]
            syltotal += tweetdict[word]
            sentence2.append(word)
        elif syltotal == 12:
            sentence2.append(word)
    index += 1
    for item in tweet[index:]:
        sentence3.append(word)
    
    return sentence1, sentence2, sentence3    
            
            
