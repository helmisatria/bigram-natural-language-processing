# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:27:19 2018

@author: user
"""

import pandas
import numpy as np
import re


data = pandas.read_csv('data.csv')

articles = data['article']

bagOfWords = []

for i, article in enumerate(articles):
    clean_article = re.sub('[–"!@#$%()&+,./;:=“”\'0123456789‘-]', '', article)
    
    bagOfWords.append(clean_article.lower().split())

bagOfWords = np.concatenate(bagOfWords)

unique_bagOfWords = np.unique(bagOfWords)

amountOfWords = []

for i, word_comparison in enumerate(unique_bagOfWords):
    count = 0
    for j, word in enumerate(bagOfWords):
        if (word_comparison == word):
            count += 1
    amountOfWords.append(count)

#for i, word_comparison in enumerate(unique_bagOfWords):
#    for j, word in enumerate(unique_bagOfWords):
#        if (word == word_comparison):
            