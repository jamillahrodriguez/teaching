#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lecture 17: Reviewing corpora
LING 401
Spring 2023
Jamillah Rodriguez
Mar 9 2023
"""


## Let's review how to import external corpora

### To use non-NLTK data, you need to do either of the following:
# 1. Manually drag the file(s) you are using to your current directory. OR
# 2. Change your current directory to the folder with the file in it.

import os # We need this package to look at our location

# Option 1. Our current directory. This will be wherever your current .py or .ipynb file is.
# If your file is already in here, great!
os.listdir('.')


# Or 2. You can change your directoy. This needs to match the folder your file is in.
os.chdir('/Users/jamillahrodriguez/Desktop')

# Now you need to read the file.
English401 = open('LING401English.txt') # This will 'open' the file and save it to a workable object

English401String = English401.read() # This will allow us to read that object
print(English401String)

# Note: For corpora outside of English.
# You may need to worry about encoding (depending on what you're doing)

Korean401 = open('LING401Korean.txt')

Korean401String = Korean401.read()
print(Korean401String)

# Some of the functions we learned will still work
print(Korean401String[:10])

Korean401List = Korean401String.split()
[word for word in Korean401List if word.endswith("을") or word.endswith("를")] # This works!

Korean401String.count("ㄱ") # This does not.

# Returning to corpora we have looked at!

from nltk.corpus import gutenberg

# .raw() will get the data as it originally was (no fancy stuff done)
gutenberg.raw("carroll-alice.txt")[:500] # This will get the first 500 characters of that raw text (including \n for 'new line')

# Many of the corpora in NLTK have a pre-defined .words() function to get "words:
gutenberg.words("carroll-alice.txt")

# If you are working with a corpus without this pre-defined function, remember we also have the .word_tokenize() function
from nltk.tokenize import word_tokenize
aliceWords = word_tokenize(gutenberg.raw("carroll-alice.txt"))

# As well as a pre-defined function to get the sentences:
gutenberg.sents("carroll-alice.txt")

# Other helpful NLTK corpora
import nltk
from nltk.book import *

text1.concordance("monstrous")

text1.similar("monstrous")

text2.similar("monstrous")

text2.common_contexts(["monstrous", "very"])


# Brown corpus
from nltk.corpus import brown

romanceSents = brown.sents(categories = "romance")
print(romanceSents)

romanceWords = brown.words(categories = "romance")
print(romanceWords)


# CMU dictionary

pronList = nltk.corpus.cmudict.entries()
pronList[500]

prondict = nltk.corpus.cmudict.dict()
prondict['fire']

# Wordnet

from nltk.corpus import wordnet as wn 

wn.synsets("horse")

wn.synset('horse.n.01').lemma_names()