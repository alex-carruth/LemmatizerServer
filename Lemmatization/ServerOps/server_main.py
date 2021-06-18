# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:10:37 2021

@author: acarr
"""
from Lemmatizers import server_wordnet_lemma
import json

def switch_function(sentence_json):
    switches = {
            "wordnet": run_wordnet
        }
    validFlag = False;
    for item in switches:
        if(item == sentence_json["function"]):
            validFlag = True
    if(validFlag == False):
        print("Invalid function")
        return sentence_json
    return_json = switches[sentence_json["function"]](sentence_json)
    return return_json

def run_wordnet(sentence_json):
    return_json = server_wordnet_lemma.lemmatize(sentence_json)
    return return_json