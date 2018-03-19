#!/usr/bin/python3

import gzip
import json
import re
import nltk
from random import *
 
    
#def get_syl(string):
    #"""Returns a list of the syllables of the words in the tweet."""


def count_syl(tweet:
    """Counts the syllables of a tweet."""


#def generate_haiku(syllables):
    #"""Converts a tweet into a haiku."""


def tokenize(text):
    sent_split = re.compile('[^ ].*?[.!?]\'?')
    sentences = sent_split.findall(text)
    tokens = [" ".join(nltk.word_tokenize(sentences[i], "dutch"))
              for i in range(len(sentences))]
    tokens = [re.sub(r"'([^ 0-9])", r"' \1", token) for token in tokens]
    return tokens


def main():
    list_tweets = []
    with gzip.open('/net/corpora/twitter2/Tweets/Tekst/2018/03/20180301:00.out.gz', "rt") as tweets:
        for line in tweets:
            list_tweets.append(tokenize(line)[1:])
    tweet = list_tweets[randrange(0, len(list_tweets))]
    number_syl = 0
    for word in tweet:
        number_syl = numb_syl + count_syl(word)
    if number_syl 
        tweet = list_tweets[randrange(0, len(list_tweets))]
        for word in tweet:
            number_syl = numb_syl + count_syl(word)
    else:
        print(tweet)


if __name__ == "__main__":
    main()
