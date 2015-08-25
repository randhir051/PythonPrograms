#!/usr/bin/python

from nltk.metrics import edit_distance
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet
from nltk.corpus import words
tokenizer = RegexpTokenizer("[\w']+")
inputTextTokenized = tokenizer.tokenize("correc is weird")
for token in inputTextTokenized:
	syn = wordnet.synsets(token)
	if(len(syn)==0):
		for word in words.words('en'):
			if edit_distance(token,word)<3:
				print word			