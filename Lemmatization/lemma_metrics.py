# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:36:59 2021

@author: acarr
"""
import pandas as pd
import math
def score_checker(csv_name):
    df = pd.read_csv(csv_name)
    true = 0
    total_pos = 0
    pos_true = 0
    for index, row in df.iterrows():
        lemma = row[0]
        if(not lemma != lemma):
            lemma = lemma.lower()
        orlem = row[1]
        if(not orlem != orlem):
            orlem = orlem.lower()
        original = row[2]
        if(not original != original):
            original = original.lower()
        if(lemma == orlem):
            true += 1
        if(lemma != orlem and lemma != original and not original != original):
            total_pos += 1
            #print("%s   %s" % (lemma,orlem))
        elif(lemma == orlem and lemma != original and not original != original):
            pos_true += 1
            total_pos += 1
    precision = true/len(df)
    recall = pos_true/total_pos
    f1 = 2 * (precision * recall)/(precision + recall)
    return precision, recall, f1
#%%
#Genia Score
genia_p, genia_r, genia_f = score_checker("genia_accuracy.csv")
print("Genia Precision: %1.3f   Genia Recall: %1.3f   Genia F1-Score: %1.3f" % (genia_p, genia_r, genia_f))

#%%
#WordNet Score
wordnet_p, wordnet_r, wordnet_f = score_checker("wordnet_accuracy.csv")
print("WordNet Precision: %1.3f   WordNet Recall: %1.3f   WordNet F1-Score: %1.3f" % (wordnet_p, wordnet_r, wordnet_f))

#%%
#LuiNorm Score
luinorm_p, luinorm_r, luinorm_f = score_checker("luinorm_accuracy.csv")
print("LuiNorm Precision: %1.3f   LuiNorm Recall: %1.3f   LuiNorm F1-Score: %1.3f" % (luinorm_p, luinorm_r, luinorm_f))

#%%
#SciSpaCy Score
scispa_p, scispa_r, scispa_f = score_checker("scispacy_accuracy.csv")
print("SciSpaCy Precision: %1.3f   SciSpaCy Recall: %1.3f   SciSpaCy F1-Score: %1.3f" % (scispa_p, scispa_r, scispa_f))

#%%
#Stanza Score
stanza_p, stanza_r, stanza_f = score_checker("stanza_accuracy.csv")
print("Stanza Precision: %1.3f   Stanza Recall: %1.3f   Stanza F1-Score: %1.3f" % (stanza_p, stanza_r, stanza_f))
