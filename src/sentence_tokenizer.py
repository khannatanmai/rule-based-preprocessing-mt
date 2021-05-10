import spacy
import sys

nlp = spacy.load('en_core_web_sm') # Load the English Model

file_name = sys.argv[1]
f = open(file_name).readlines()

for line in f:
	doc = nlp(line)
	for sent in doc.sents:
		print(str(sent).strip())

