#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lecture 14: N-grams
LING 401
Spring 2023
Jamillah Rodriguez
Feb 28 2023
"""

# How can we estimate the probability of a word given its context?

import nltk
from nltk.corpus import gutenberg
emma = gutenberg.raw('austen-emma.txt').lower() 

# We can calculate the probability of getting "recovering" after "there was no" fairly easily!

emma.count("there was no recovering")/emma.count("there was no")

emma.count("there was no")

emma.count("there was no recovering")


# Individual exercise: Now find the probability of getting the following.

# 1. "advice" after "very good" in "carrol-alice.txt"
# 2. "heads" after "off with their" in "carrol-alice.txt"
# 3. "advice" after "very good" in "austen-emma.txt"
# 4. "heads" after "off with their" in "austen-emma.txt"


# Thank you NLTK! There's a built-in n-grams function.
sent = ["Colorless", "green", "ideas", "sleep", "furiously"]
list(nltk.bigrams(sent))

list(nltk.trigrams(sent))


# To get larger n-grams, you can import the ngrams package from nltk.util
from nltk.util import ngrams
sent = "Atlas laughed so loudly that the colorless green ideas became furious".split()
list(ngrams(sent, 5))

# But for many tasks we may also want/need to know sentence boundaries...

from nltk.util import pad_sequence
padded_sent = list(pad_sequence(sent, pad_left=True, left_pad_symbol="<s>", pad_right=True, right_pad_symbol="</s>", n = 2))

print(padded_sent)

list(ngrams(padded_sent,4))

# Simplest Markov assumption: unigrams
# Modeling a language based only on probability of individual words
emma = gutenberg.words("austen-emma.txt")

import random # This package contains the random.choice() function

emmaUnigramsLM = [random.choice(emma) for i in range(100)]
print(" ".join(emmaUnigramsLM))


# Let's try instead with bigrams
# Remember that we can create frequency distributions to look at how often each bigram occurs

emmaBigrams = list(nltk.bigrams(emma))
fdBigrams = nltk.FreqDist(emmaBigrams)
fdBigrams.most_common()


cfdBigrams = nltk.ConditionalFreqDist(emmaBigrams)
cfdBigrams['living'] # We'll come back to this next class.

emmaBigramsLM = [" ".join(random.choice(emmaBigrams)) for i in range(100)]
print(" ".join(emmaBigramsLM))


# And now with trigrams
emmaTriLM = [" ".join(random.choice(emmaTri)) for i in range(100)]
print(" ".join(emmaTriLM))
