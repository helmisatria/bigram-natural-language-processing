# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:27:19 2018

@author: user
"""

import pandas
import numpy as np
import re
import collections
import math

data = pandas.read_csv('data-tmp.csv')

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
                
                bigram_counts[i][j] += 2

# Laplace smoothing

bigram_counts[bigram_counts > 0 ] += 1
bigram_counts[bigram_counts == 0 ] = 1

# Compute Bigram Probabilities

bigram_probabilities = np.zeros((len(unique_bagOfWords), len(unique_bagOfWords)), dtype=float)

for i, bigramCountX in enumerate(bigram_counts):
    
    for j, count in enumerate(bigramCountX):

        bigram_probabilities[i][j] = count/(counter_word[unique_bagOfWords[i]] + len(unique_bagOfWords))

sentence = 'Bank Indonesia BI akan memantau'.lower().split()

sumOfLog = 0

for i, word in enumerate(sentence):
    
    if (i == len(sentence) - 1): break
    
    word_index1 = unique_bagOfWords.tolist().index(word)
    word_index2 = unique_bagOfWords.tolist().index(sentence[i + 1])
    
    prob = bigram_probabilities[word_index1, word_index2]
    log = math.log2(prob)
    
    sumOfLog += log
    
print('Sum of Log ', sumOfLog)

l = 1/len(sentence) * sumOfLog
perplexity = math.pow(2, -1 * l)

print('Perplexity: ', perplexity)

# Perplexity = 2 pangkat -l, l = 1/M * (Sum of Log)

print('Index Agustus: ' + str(unique_bagOfWords.tolist().index('agustus')))
print('Index Akhir: ' + str(unique_bagOfWords.tolist().index('akhir')))

print('Prob: ' +str(bigram_probabilities[unique_bagOfWords.tolist().index('agustus'), unique_bagOfWords.tolist().index('akhir')]))

pandas.DataFrame(bigram_probabilities).to_csv('Bigram_Probabilities.csv', index=False, header=False)
pandas.DataFrame(unique_bagOfWords).to_csv('BagOfWords.csv', index=False, header=False)
    
        

