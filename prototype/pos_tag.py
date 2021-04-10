import spacy
import sys
from queue import Queue

#Reading rule set
rule_file = open("rule-set.ppr")
rule_lines = rule_file.readlines()

pattern_input = ""
replacement_input = ""

for line in rule_lines:
	line = line.strip()

	if "->" not in line:
		sys.exit() #Only one rule for now

	rule = line.strip()
	rule = rule.split("->")

	pattern_input = rule[0].strip()
	replacement_input = rule[1].strip()


nlp = spacy.load("en_core_web_sm")

text = sys.argv[1]
doc = nlp(text)
arguments = {}

pattern_tokens = pattern_input.split(" ")
replacement_tokens = replacement_input.split(" ")

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

for token in doc:
	input_buffer.put(str(token))

	pair_to_check = detection_pattern[detection_index]

	#Matching one word from the pattern (index -> detection index)
	if(pair_to_check[1] == 0): #CHECK STRING
		if(pair_to_check[0] == str(token)):
			detection_index += 1
		else:
			detection_index = 0
			while(not input_buffer.empty()):
				output_sentence.append(input_buffer.get())

			continue

	elif(pair_to_check[1] == 1): #CHECK POS TAG
		temp_arg = ""
		pos_to_check = ""

		if(pair_to_check[0][-2] == "@"): #argument number mentioned
			temp_arg = pair_to_check[0][-1]
			pos_to_check = pair_to_check[0][:-2]
		else:
			pos_to_check = pair_to_check[0]

		if(pos_to_check == str(token.tag_)):
			detection_index += 1
			arguments[temp_arg] = str(token)
		else:
			detection_flag = 0
			while(not input_buffer.empty()):
				output_sentence.append(input_buffer.get())

			continue

	if(detection_index >= len(detection_pattern)):
		detection_flag = True

		for rep_token in replacement_tokens: #Add replacement construction to output
			if(rep_token[0] == "[" and rep_token[1] == "@" and rep_token[-1] == "]"):
				arg_to_get = rep_token[2]
				output_sentence.append(arguments[arg_to_get])
			else:
				output_sentence.append(rep_token)

		while(not input_buffer.empty()): #Discard original construction
			input_buffer.get() 

		detection_index = 0

# Flushing buffer
while(not input_buffer.empty()):
	output_sentence.append(input_buffer.get())

if(detection_flag):
	print(" ".join(output_sentence))
else:
	print(text)

