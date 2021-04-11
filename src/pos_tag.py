import spacy
import sys

nlp = spacy.load("en_core_web_sm")

text = sys.argv[1]
doc = nlp(text)

for token in doc:
	print(token, token.tag_)