#!/usr/bin/python3
# File name: acc_haiku.py
# This program automatically tweets a tweet in haiku form,
# randomly chosen from a database of Dutch tweets.
# Authors:   Thomas Tan, Jan Harms, Gijs Danoe, Inge Salomons
# Date:      10 April, 2018


import re
import gzip
import nltk
import pickle
import tweepy
from keys import *
from random import *
from nltk.tokenize.moses import MosesDetokenizer


def word_check(tweet, tweetdict):
    """Checks if the words in the tweet are in the CELEX dictionary."""
    for word in tweet:
        if word.lower() not in tweetdict:
            return False
    return True


def count_check(tweet, tweetdict):
    """Checks if a tweet consists of exactly 17 syllables."""
    if not word_check(tweet, tweetdict):
        return False
    else:
        total_count = 0
        for word in tweet:
            total_count += tweetdict[word.lower()]
        if total_count == 17:
            return True
        else:
            return False


def haiku_check(tweet, tweetdict):
    """Checks if a tweet is compatible with the haiku format (5-7-5)."""
    if not count_check(tweet, tweetdict):
        return False
    if tweet == []:
        return False
    index = 0
    syltotal = tweetdict[tweet[index].lower()]
    while True:
        if syltotal < 5:
            index += 1
            syltotal += tweetdict[tweet[index].lower()]
        elif syltotal == 5:
            break
        else:
            return False
    index += 1
    syltotal += tweetdict[tweet[index].lower()]
    while True:
        if syltotal < 12:
            index += 1
            syltotal += tweetdict[tweet[index].lower()]
        elif syltotal == 12:
            return True
        else:
            return False


def generate_haiku(tweet, tweetdict):
    """Transforms a tweet into three haiku sentences."""
    sentence1 = [tweet[0]]
    sentence2 = []
    sentence3 = []
    index = 0
    syltotal = tweetdict[tweet[index].lower()]
    while True:
        if syltotal < 5:
            index += 1
            syltotal += tweetdict[tweet[index].lower()]
            sentence1.append(tweet[index])
        elif syltotal == 5:
            break
    index += 1
    if tweet[index] in "-.!?,:;)'\"":
        sentence1.append(tweet[index])
        index += 1
    syltotal += tweetdict[tweet[index].lower()]
    while True:
        if syltotal < 12:
            sentence2.append(tweet[index])
            index += 1
            syltotal += tweetdict[tweet[index].lower()]
        elif syltotal == 12:
            sentence2.append(tweet[index])
            break
    index += 1
    if tweet[index] in "-.!?,:;)'\"":
        sentence2.append(tweet[index])
        index += 1
    for item in tweet[index:]:
        sentence3.append(item)
    detokenizer = MosesDetokenizer()
    return [detokenizer.detokenize(sentence1, return_str=True),
            detokenizer.detokenize(sentence2, return_str=True),
            detokenizer.detokenize(sentence3, return_str=True)]


def main():
    tweetdict = pickle.load(open("dpw.p", "rb"))
    for punct in "-.!?,:;#()@/'\"":
        tweetdict[punct] = 0
    list_tweets = []
    months = ['01', '02', '03', '04', '05', '06',
              '07', '08', '09', '10', '11', '12']
    hours = months + ['13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '00']
    days = hours[:-1] + ['24', '25', '26', '27', '28']
    with gzip.open(
        "/net/corpora/twitter2/Tweets/Tekst/"
        "20{0}/{1}/20{0}{1}{2}:{3}.out.gz"
        .format(randrange(11, 18), months[randrange(0, len(months))],
                days[randrange(0, len(days))],
                hours[randrange(0, len(hours))]), "rt") as tweets:
        for line in tweets:
            line = nltk.word_tokenize(line, "dutch")
            list_tweets.append(line)
    tweet_u = list_tweets[randrange(0, len(list_tweets))]
    tweet = tweet_u[1:]
    while not haiku_check(tweet, tweetdict):
        tweet_u = list_tweets[randrange(0, len(list_tweets))]
        tweet = tweet_u[1:]
    [sentence1, sentence2, sentence3] = generate_haiku(tweet, tweetdict)
    sentence1 = sentence1.replace("# ", "#")
    sentence2 = sentence2.replace("# ", "#")
    sentence3 = sentence3.replace("# ", "#")
    print("#accidentalhaiku door {0}:\n{1}\n{2}\n{3}".format(tweet_u[0],
          sentence1, sentence2, sentence3))

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(akey, asecret)

    api = tweepy.API(auth)
    api.update_status(
        "#accidentalhaiku door {0}:\n{1}\n{2}\n{3}"
        .format(tweet_u[0], sentence1, sentence2, sentence3))


if __name__ == "__main__":
    main()
