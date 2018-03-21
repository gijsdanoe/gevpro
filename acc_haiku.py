#!/usr/bin/python3

import gzip
import re
import nltk
from random import *


def count_syl(tweet):
    """Counts the syllables of a tweet."""


def count_check(tweet, tweetdict):
    total_count = 0
    for word in tweet:
        total_count = total_count + tweetdict[word]
    if total_count == 17:
        return True
    else:
        return False


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


def generate_haiku(tweet, tweetdict):
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
    

def tokenize(text):
    sent_split = re.compile('[^ ].*?[.!?]\'?')
    sentences = sent_split.findall(text)
    tokens = [" ".join(nltk.word_tokenize(sentences[i], "dutch"))
              for i in range(len(sentences))]
    tokens = [re.sub(r"'([^ 0-9])", r"' \1", token) for token in tokens]
    return tokens


def main():
    list_tweets = []
    with gzip.open('/net/corpora/twitter2/Tweets/Tekst/2018/03/20180301:15.out.gz', "rt") as tweets:
        for line in tweets:
            list_tweets.append(tokenize(line)[1:])
    tweet = list_tweets[randrange(0, len(list_tweets))]
    syl_info = count_syl(tweet)
    while not count_check(syl_info) and haiku_check(tweet, syl_info):
        tweet = list_tweets[randrange(0, len(list_tweets))]
        syl_info = count_syl(tweet)
    sentence1, sentence2, sentence3 = generate_haiku(tweet, syl_info)
    print("{0}\n{1}\n{2}".format(" ".join(sentence1), " ".join(sentence2), " ".join(sentence3)))


if __name__ == "__main__":
    main()
