# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:38:58 2021

@author: acarr
"""
import pandas as pd
import os, sys

#Get text to lemmatize from the file lemmatize_text file
original_generator= []
with open("lemmatize_text.txt", "r") as a_file:
    for line in a_file:
        stripped_line = line.split()
        for original in stripped_line:
            original_generator.append(original)
original_dataframe = pd.DataFrame(original_generator, columns=['Original'])
original_dataframe.to_csv("original_csv.csv", header=['Original'], index=False)