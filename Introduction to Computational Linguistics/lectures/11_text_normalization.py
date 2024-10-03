"""
Lecture 11: Text normalization
LING 401
Spring 2023
Jamillah Rodriguez
Feb 16 2023
"""


# Stopwords

from nltk.corpus import brown
from nltk.probability import FreqDist

words = [w.lower() for w in brown.words() if w.isalpha()]
wordFreq = FreqDist(words)
wordFreq.most_common()[:20]


from nltk.corpus import stopwords
stopwords.words("english")
stopwords.words("spanish")


# How many stopwords in the following sentence?
x = "the cat's tail was being pulled and the cat was angry".split()
print(x)

stopwords = stopwords.words("english")
x_nostop = [word for word in x if word not in stopwords]
print(x_nostop)


brownWords = [word.lower() for word in brown.words() if word.isalpha()]
len(brownWords)

words_nostops = [word for word in brownWords if word not in stopwords]
len(words_nostops)

len(words_nostops)/len(brownWords) # About 50% stopwords!

# How can we get words from a text?

from nltk.corpus import gutenberg
alice = gutenberg.raw("carroll-alice.txt")
print(alice)


aliceWords = alice.split()
print(aliceWords)

# Good news! NLTK has a built-in word tokenizer.

from nltk.tokenize import word_tokenize
aliceToken = word_tokenize(alice)
print(aliceToken) # What differences do you notice here?



# Stemming

from nltk.corpus import brown
import re

[word for word in set(brown.words()) if re.search("^..ing$", w)]

# Good news! NLTK has a built-in porter stemmer
from nltk.stem import PorterStemmer
ps = PorterStemmer()

x = "The cat's tail was being pulled and the cat was angry"
x = word_tokenize(x)
print([ps.stem(word) for word in x])

# Let's try on a larger text
aliceTokens = word_tokenize(alice)
print([ps.stem(word) for word in aliceTokens])

