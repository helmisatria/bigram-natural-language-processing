# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 00:28:40 2018

@author: user
"""

import numpy as np
import pandas

unique_bagOfWords = pandas.read_csv('bagOfWords.csv', names=['words'])['words'].tolist()
bigram_probabilities = pandas.read_csv('Bigram_Probabilities.csv', header=None).values.tolist()


kata = ''
while (kata != '99'):    
    kata = input("Masukkan kata: ")
    
    if (kata in unique_bagOfWords):
#        print('kata tersedia')
        
        word_index = unique_bagOfWords.index(kata)
        
        max_probabilities = np.max(bigram_probabilities[word_index])
        
        next_word_index = bigram_probabilities[word_index].index(max_probabilities)
        
        print('next word: ' + unique_bagOfWords[next_word_index])
        
    else:
        print('kata tidak ditemukan')
         