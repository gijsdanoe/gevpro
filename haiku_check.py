#!/usr/bin/python3

def haiku_check(tweet, tweetdict):

    index = 0
    word = tweet[index]
    syltotal = tweetdict[word]
    while True:
        if syltotal < 5:
            index +=1
            word = tweet[index]
            syltotal += tweetdict[word]
        elif syltotal == 5:
            break
        else:
            return False
    index +=1
    word = tweet[index]
    syltotal += tweetdict[word]
    while True:
        if syltotal < 12:
            index +=1
            word = tweet[index]
            syltotal += tweetdict[word]
        elif syltotal == 12:
            return True
        else:
            return False
                    
