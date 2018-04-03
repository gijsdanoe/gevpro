#!/usr/bin/python3

import gzip
import re
import nltk
import pickle
from random import *

def word_check(tweet, tweetdict):
    for word in tweet:
        if word not in tweetdict:
            return False
        elif word in "-.!?,:;#()@/0123456789'\"":
            pass
    return True


def count_check(tweet, tweetdict):
    """Checks if a tweet consists of exactly 17 syllables."""
    total_count = 0
    for word in tweet:
        if word not in "-.!?,:;#()@/0123456789'\"":
            total_count = total_count + tweetdict[word]
    if total_count == 17:
        return True
    else:
        return False

def haiku_check(tweet, tweetdict):
    """Checks if a tweet is compatible with the haiku format (5-7-5)"""
    if tweet == []:
        return False
    index = 0
    word = tweet[index]
    syltotal = tweetdict[word]
    while True:
        word = word.lower()
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


def generate_haiku(tweet, tweetdict):
    """Transforms a tweet into three haiku sentences"""
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
            break
    index +=1
    word = tweet[index]
    syltotal += tweetdict[word]
    while True:
        if syltotal < 12:
            sentence2.append(word)
            index +=1
            word = tweet[index]
            syltotal += tweetdict[word]
        elif syltotal == 12:
            sentence2.append(word)

            break
    index += 1
    word = tweet[index]
    for item in tweet[index:]:
        sentence3.append(word)
    return sentence1, sentence2, sentence3   
    
# niet goed

def tokenize(text):
    sent_split = re.compile('[^ ].*?[ .!?]\'?')
    sentences = sent_split.findall(text)
    tokens = [" ".join(nltk.word_tokenize(sentences[i], "dutch"))
              for i in range(len(sentences))]
    tokens = [re.sub(r"'([^ 0-9])", r"' \1", token) for token in tokens]
    return tokens


def main():
    words = pickle.load(open("dpw.p", "rb"))
    tweetdict = words
    list_tweets = []
    with open('/net/corpora/twitter2/Tweets/Tekst/2018/04/20180403:16.out', "rt") as tweets:
        for line in tweets:
            line = line.lower()
            line = tokenize(line)
            line = " ".join(line)
            list_tweets.append(line.split(' '))
    tweet = list_tweets[6749]
    print(tweet)
    while True:
        if word_check(tweet, words) == False: 
            tweet
        elif count_check(tweet, words) == False:
            tweet
        elif haiku_check(tweet, words) == False:
            tweet
        else:
            break
    sentence1, sentence2, sentence3 = generate_haiku(tweet, words)
    print("{0}\n{1}\n{2}".format(" ".join(sentence1), " ".join(sentence2), " ".join(sentence3)))


if __name__ == "__main__":
    main()