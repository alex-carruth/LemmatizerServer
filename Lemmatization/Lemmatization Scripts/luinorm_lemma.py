
#LuiNorm
import os, sys
from luinormwrapper import LuiNormTagger
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

#Get directory of Lui9Norm
directory = "D:\Coding\BioMojo\Lemmatization\luinormtagger\lvg2021\lvg2021\\bin"
tagger = LuiNormTagger(directory)

luinorm_generator = []
#Tag the words, create a dataframe and put it into a csv
for word in tagger.tag(sentence):
    luinorm_generator.append(word)
luinorm_dataframe = pd.DataFrame(luinorm_generator, columns=['LuiNorm'])
luinorm_dataframe.to_csv("luinorm.csv", header=['LuiNorm'], index=False)
#%%