import ebooklib
from ebooklib import epub
import re
import os
import nltk
import numpy as np
from nltk.corpus import words
from nltk.corpus import words, stopwords, names
import gensim
from nltk.stem import WordNetLemmatizer

english_vocab = set(w.lower() for w in nltk.corpus.words.words())
def is_english_word(word):
    # Initialize the Enchant English dictionary
    return (word in english_vocab)
stop_words = stopwords.words("english")

def preprocess(paragraphs):
    words=[]
    filtered_words=[]
    lemmatized_words=[]
    processeddoc=[]
    
    for i in paragraphs:
        words.append(gensim.utils.simple_preprocess(i, min_len = 3, deacc=True)) 
        lemmatizer = WordNetLemmatizer()
    
    for i in range (0,len(words)):
        lemmatized_words.append([lemmatizer.lemmatize(word) for word in words[i]])

    for i in range (0,len(lemmatized_words)):
        filtered_words.append([word for word in lemmatized_words[i] if ((word not in stop_words)and(is_english_word(word)))]) 
    
    for i in range(0,len(filtered_words)):
        processeddoc.append(" ".join(filtered_words[i]))
        
    return processeddoc



class preprocessmodel:
    def __init__(self,textlist):
        preprocess_text_list=preprocess(textlist)