#!/usr/bin/python3

import gzip
import re
import nltk
from random import *


def count_syl(tweet):
    """Counts the syllables of a tweet."""


def count_check(tweet):
    total_count = 0
    for word in tweet:
        total_count = total_count + tweet[word]
    if total_count == 17:
        return True
    else:
        return False


def haiku_check(tweet):


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
    tweet = list_tweets[randrange(0, len(list_tweets))])
    syl_info = count_syl(tweet)
    while not count_check(syl_info) and haiku_check(tweet, syl_info):
        tweet = list_tweets[randrange(0, len(list_tweets))])
        syl_info = count_syl(tweet)
    print(tweet)


if __name__ == "__main__":
    main()
