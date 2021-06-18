# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:46:47 2021

@author: acarr
"""
# Word Net
import nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('punkt')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import os,sys
import pandas as pd

#Get text to lemmatize from the file lemmatize_text file
sentence = ""
i = 0
with open("lemmatize_text.txt", "r") as a_file:
    for line in a_file:
        stripped_line = line.split()
        for word in stripped_line:
            if(i > 0):
                sentence = sentence + " " + word
            else:
                sentence = word
                i += 1

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


#Init Lemmatizer
lemmatizer = WordNetLemmatizer()

#Lemmatize a Sentence with the appropriate POS tag
#print([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sentence)])
#Tag the words, create a dataframe and put it into a csv
wordnet_generator = []
#Tag the words, create a dataframe and put it into a csv
for word in nltk.word_tokenize(sentence):
    wordnet_generator.append(lemmatizer.lemmatize(word,get_wordnet_pos(word)))
wordnet_dataframe = pd.DataFrame(wordnet_generator, columns=['WordNet'])
wordnet_dataframe.to_csv("wordnet.csv", header=['WordNet'], index=False)