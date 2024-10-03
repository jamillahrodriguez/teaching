#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lecture 23: Context Free Grammars
LING 401
Spring 2023
Jamillah Rodriguez
April 4 2023
"""


# Let's see what NLTK can do!

import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")

# Creates a parser using your rules
parser = nltk.ChartParser(grammar)

# Prints the constituents/tree in bracket notation
sent = ["I", "shot", "an", "elephant"]
for tree in parser.parse(sent):
    print(tree)
    
# Draws the tree
for tree in parser.parse(sent):
    tree.draw()

# What happens if we get a tree not supported by the grammar?
sent = ["I", "really", "love", "coffee"]
for tree in parser.parse(sent):
    print(tree)
    
sent = ["An", "elephant", "shot", "my", "pajamas"] 
# What will this do?
for tree in parser.parse(sent):
    print(tree)

# What happens if we give the parser an ambiguous sentence?
pjs = ["I", "shot", "an", "elephant", "in", "my", "pajamas"]
for tree in parser.parse(pjs):
    print(tree)
    
for tree in parser.parse(pjs):
    tree.draw()
    
# If you have many rules, you can create a larger grammar!
# Reminder: The mygrammar.cfg file must be in the same location as your current .py file!
grammar = nltk.data.load('file:mygrammar.cfg')
sent = "I shot an elephant in my pajamas".split()
parser = nltk.ChartParser(grammar)
for tree in parser.parse(sent):
    print(tree)

# UPenn Treebanks
from nltk.corpus import treebank

t = treebank.parsed_sents('wsj_0010.mrg')[0]
print(t)
t.draw()