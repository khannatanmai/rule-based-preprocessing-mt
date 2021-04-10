import spacy
import sys
from queue import Queue

nlp = spacy.load("en_core_web_sm")

text = sys.argv[1]
doc = nlp(text)

pattern_input = sys.argv[2]
pattern_tokens = pattern_input.split(" ")

# preparing pattern for detection
detection_pattern = []
for i in pattern_tokens:
	if(i[0] == "[" and i[-1] == "]"):
		detection_pattern.append((i[1:-1],1)) #type 1: POS tag
	else:
		detection_pattern.append((i,0)) #type 0: String

# detection in source sentence
detection_flag = False
detection_index = 0

input_buffer = Queue(maxsize = 0)

output_sentence = []
arguments = []


for token in doc:
	print(token, token.tag_)
	input_buffer.put(str(token))

	pair_to_check = detection_pattern[detection_index]

	#Matching one word from the pattern (index -> detection index)
	if(pair_to_check[1] == 0):
		if(pair_to_check[0] == str(token)):
			detection_index += 1
		else:
			detection_index = 0
			while(not input_buffer.empty()):
				output_sentence.append(input_buffer.get())

			continue

	elif(pair_to_check[1] == 1):
		if(pair_to_check[0] == str(token.tag_)):
			detection_index += 1
		else:
			detection_flag = 0
			while(not input_buffer.empty()):
				output_sentence.append(input_buffer.get())

			continue

	if(detection_index >= len(detection_pattern)):
		print("Found a pattern!")
		detection_index = 0

#print(output_sentence)
#print(detection_pattern)

