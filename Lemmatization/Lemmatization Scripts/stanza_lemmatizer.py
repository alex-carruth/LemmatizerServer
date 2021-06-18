#from google.colab import files
#uploaded = files.upload()

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
#Stanza
#!pip install Stanza
import stanza
#stanza.download('en', package='mimic', processors={'ner': 'i2b2'} )
nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'i2b2'})
doc = nlp(sentence)
#print(*[f'lemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
stanza_generator = []
#Tag the words, create a dataframe and put it into a csv
for sent in doc.sentences:
  for word in sent.words:
    stanza_generator.append(word.lemma)
stanza_dataframe = pd.DataFrame(stanza_generator, columns=['Stanza'])
stanza_dataframe.to_csv("stanza.csv", header=['Stanza'], index=False)
