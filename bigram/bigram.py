# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:27:19 2018

@author: user
"""

import pandas
import numpy as np
import re
import collections

data = pandas.read_csv('data.csv')

articles = data['article']

bagOfWords = []

for i, article in enumerate(articles):
    clean_article = re.sub('[–"!@#$%()&+,./;:=“”\'0123456789‘-]', '', article)
    
    bagOfWords.append(clean_article.lower().split())


bagOfWords = np.concatenate(bagOfWords)


unique_bagOfWords = np.unique(bagOfWords)

amountOfWords = []

counter_word = collections.Counter(bagOfWords)

# Compute raw Bigram Counts

bigram_counts = np.zeros((len(unique_bagOfWords), len(unique_bagOfWords)), dtype=int)

for z, wordArticle in enumerate(bagOfWords):
    print('z: ' + str(z))
    
    if (z == len(bagOfWords) - 1):
        break
    
    for i, wordX in enumerate(unique_bagOfWords):
        
        for j, wordY in enumerate(unique_bagOfWords):
            
            if (wordX != wordArticle):
                break
                        
            if (wordX == wordArticle and wordY == bagOfWords[z + 1]):
                
                bigram_counts[i][j] += 1
            

bigram_probabilities = np.zeros((len(unique_bagOfWords), len(unique_bagOfWords)), dtype=float)

for i, bigramCountX in enumerate(bigram_counts):
    
    for j, count in enumerate(bigramCountX):
        
        index = i
        if (i > len(unique_bagOfWords)):
            index = i * j
                
        bigram_probabilities[i][j] = count/counter_word[unique_bagOfWords[index]]


pandas.DataFrame(bigram_probabilities).to_csv('Bigram_Probabilities.csv', index=False, header=False)
pandas.DataFrame(unique_bagOfWords).to_csv('BagOfWords.csv', index=False, header=False)
    
        

