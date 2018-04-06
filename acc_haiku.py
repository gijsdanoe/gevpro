#!/usr/bin/python3
# File name: acc_haiku.py
# This program automatically tweets a tweet in haiku form,
# randomly chosen from a Dutch database of tweets.
# Authors:   Thomas Tan, Jan Harms, Gijs Danoe, Inge Salomons
# Date:      11 April, 2018

import tweepy
from keys import *
import gzip
import re
import nltk
import pickle
from random import *
from time import sleep


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
    word = tweet[index]
    syltotal = tweetdict[word.lower()]
    while True:
        if syltotal < 5:
            index += 1
            word = tweet[index]
            syltotal += tweetdict[word.lower()]
        elif syltotal == 5:
            break
        else:
            return False
    index += 1
    word = tweet[index]
    syltotal += tweetdict[word.lower()]
    while True:
        if syltotal < 12:
            index += 1
            word = tweet[index]
            syltotal += tweetdict[word.lower()]
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
    syltotal = tweetdict[word.lower()]
    while True:
        if syltotal < 5:
            index += 1
            word = tweet[index]
            syltotal += tweetdict[word.lower()]
            sentence1.append(word)
        elif syltotal == 5:
            break
    index += 1
    word = tweet[index]
    syltotal += tweetdict[word.lower()]
    while True:
        if syltotal < 12:
            sentence2.append(word)
            index += 1
            word = tweet[index]
            syltotal += tweetdict[word.lower()]
        elif syltotal == 12:
            sentence2.append(word)

            break
    index += 1
    for item in tweet[index:]:
        sentence3.append(item)
    return sentence1, sentence2, sentence3


def main():
    counter = 0
    while True:
        if counter == 15:
            break
        words = pickle.load(open("dpw.p", "rb"))
        tweetdict = words
        for mark in "-.!?,:;#()@/'\"":
            tweetdict[mark] = 0
        list_tweets = []
        months = ['01', '02', '03', '04', '05', '06',
                  '07', '08', '09', '10', '11', '12']
        hours = months + ['13', '14', '15', '16', '17', '18',
                          '19', '20', '21', '22', '23', '00']
        days = hours[:-1] + ['24', '25', '26', '27', '28']
        with gzip.open(
            "/net/corpora/twitter2/Tweets/Tekst \
            /20{0}/{1}/20{0}{1}{2}:{3}.out.gz"
            .format(randrange(11, 18), months[randrange(0, len(months))],
                    days[randrange(0, len(days))],
                    hours[randrange(0, len(hours))]), "rt") as tweets:
            for line in tweets:
                line = nltk.word_tokenize(line, "dutch")
                line = " ".join(line)
                list_tweets.append(line.split(' '))
        tweet_u = list_tweets[randrange(0, len(list_tweets))]
        tweet = tweet_u[1:]
        while not haiku_check(tweet, words):
            tweet_u = list_tweets[randrange(0, len(list_tweets))]
            tweet = tweet_u[1:]
        sentence1, sentence2, sentence3 = generate_haiku(tweet, words)
        print("Getweet door {0}:\n{1}\n{2}\n{3}".format(tweet_u[0],
              " ".join(sentence1), " ".join(sentence2), " ".join(sentence3)))
        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(akey, asecret)

        api = tweepy.API(auth)

        api.update_status(
            "Getweet door {0}:\n{1}\n{2}\n{3}"
            .format(tweet_u[0], " ".join(sentence1), " "
                    .join(sentence2), " ".join(sentence3)))
        sleep(5)
        counter += 1


if __name__ == "__main__":
    main()
