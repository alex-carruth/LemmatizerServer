# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:25:51 2021

@author: acarr
"""
#GENIA
from geniataggerwrapper import GENIATagger
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
executable_path = os.path.join('D:\\','Coding','Biomojo','Lemmatization','geniatagger','geniatagger-3.0.2',\
                               'geniatagger.exe')
directory, executable = os.path.split(executable_path)
tagger = GENIATagger(executable_path)


"""
for word, base_form, pos_tag, chunk, named_entity in tagger.tag(sentence):
    print("{:20}{:20}{:10}{:10}{:10}".format(word, base_form, pos_tag, chunk, named_entity))
"""
genia_generator = []
#Tag the words, create a dataframe and put it into a csv
for word, base_form, pos_tag, chunk, named_entity in tagger.tag(sentence):
    genia_generator.append(base_form)
genia_dataframe = pd.DataFrame(genia_generator, columns=['Genia'])
genia_dataframe.to_csv("genia.csv", header=['Genia'], index=False)
