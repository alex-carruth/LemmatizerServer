# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:58:08 2021

@author: acarr
"""
#ScispaCy
#!pip install -U spacy
#!pip install scispacy
#!pip install C:\Users\acarr\Downloads\en_core_sci_sm-0.4.0.tar.gz
#!pip install CMD-V(https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.gz)
import scispacy
import spacy
import en_core_sci_sm
from spacy import displacy
import pandas as pd
import os, sys

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

#Load the SciSpaCy model
nlp = spacy.load("en_core_sci_sm")
#Run the nlp
doc = nlp(sentence)
scispacy_generator = []
#Tag the words, create a dataframe and put it into a csv
for token in doc:
    scispacy_generator.append(token.lemma_)
scispacy_dataframe = pd.DataFrame(scispacy_generator, columns=['SciSpacy'])
scispacy_dataframe.to_csv("scispacy.csv", header=['SciSpacy'], index=False)
#%%