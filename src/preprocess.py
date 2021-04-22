import spacy
import sys

def print_to_stderr(*a):
    print(*a, file = sys.stderr)

#Argument handling
if(len(sys.argv) != 3):
	print("Error! Arguments mismatch.")
	print("Expected Input: " + sys.argv[0] + " [rule_file.ppr] [input_file.txt]")
	sys.exit(1)

rule_file_path = sys.argv[1]
input_file_path = sys.argv[2]


def check(x, y): #Comparison with multiple options
	if(x == ''): #If pattern token is [], i.e. match anything
		return True

	if "!" == x[0]: #! means NOT
		if len(x) == 1: #if input token is just !
			return (x == y)

		x_temp = x[1:] #remove !

		if "|" not in x_temp:
			return (x_temp != y)
		else:
			x_parts = x_temp.split("|")
			for i in x_parts:
				if(i == y):
					return False

			return True

	else:
		if "|" not in x:
			return (x == y)
		else:
			x_parts = x.split("|")
			for i in x_parts:
				if(i == y):
					return True

			return False

#Reading rule set
rule_file = open(rule_file_path)
rule_lines = rule_file.readlines()

patterns_and_replacements = []

for line in rule_lines:
	line = line.strip()

	if "->" not in line:
		continue

	rule = line.strip()
	rule = rule.split("->")

	pattern_tokens = rule[0].strip().split(" ")

	# Preparing pattern for detection
	detection_pattern = []
	for i in pattern_tokens:
		i_temp = i
		if(i_temp[0] == "(" and i_temp[-1] == ")"): #Optional detection token	
			if(i[1] == "[" and i[-2] == "]"):
				detection_pattern.append((i[2:-2],3)) #type 3: Optional POS tag
			elif(i[1] == "{" and i[-2] == "}"):
				detection_pattern.append((i[2:-2],5)) #type 5: Optional Lemma
			else:
				detection_pattern.append((i[1:-1],2)) #type 2: Optional String
		else:
			if(i[0] == "[" and i[-1] == "]"):
				detection_pattern.append((i[1:-1],1)) #type 1: POS tag
			elif(i[0] == "{" and i[-1] == "}"):
				detection_pattern.append((i[1:-1],4)) #type 4: Lemma
			else:
				detection_pattern.append((i,0)) #type 0: String

	patterns_and_replacements.append((detection_pattern, rule[1].strip().split(" ")))

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner", "attribute_ruler"])

input_lines = open(input_file_path).readlines()

count_input_line = 0
total_lines = len(input_lines)


for line in input_lines:
	construction_detected_in_line = False

	text = line.strip()
	count_input_line += 1
	print_to_stderr(str(count_input_line*100/total_lines) + "% Done")

	for detection_pattern, replacement_pattern in patterns_and_replacements:
		doc = nlp(text)
		arguments = {}

		# Detection in source sentence
		detection_flag = False
		detection_index = 0

		output_parts = []

		doc_index = 0
		get_input_text_idx_start = 0 # Used to get the text from the original input when a 
		# replacement happens to preserve whitespace of the remaining unreplaced text
		
		detection_text_idx_start = -1
		detection_text_idx_end = -1
		going_through_construction = False

		while(doc_index < len(doc)):
			pair_to_check = detection_pattern[detection_index]

			temp_arg = ""
			rule_token = ""
			has_arg = False

			if(len(pair_to_check[0]) >= 2):
				if(pair_to_check[0][-2] == "@"): # Variable mentioned
					temp_arg = pair_to_check[0][-1]
					rule_token = pair_to_check[0][:-2]
					has_arg = True
				else:
					rule_token = pair_to_check[0]
			else:
				rule_token = pair_to_check[0]
				

			# Matching one word from the pattern (index -> detection index)
			if(pair_to_check[1] == 0): # CHECK STRING
				if(check(rule_token, str(doc[doc_index]))):
					detection_index += 1
					if(not going_through_construction):
						detection_text_idx_start = doc[doc_index].idx
						going_through_construction = True

					if(has_arg):
						arguments[temp_arg] = str(doc[doc_index])
				else:
					detection_index = 0
					going_through_construction = False
					detection_text_idx_start = -1

			elif(pair_to_check[1] == 1): # CHECK POS TAG
				if(check(rule_token, str(doc[doc_index].tag_))):
					detection_index += 1
					if(not going_through_construction):
						detection_text_idx_start = doc[doc_index].idx
						going_through_construction = True

					if(has_arg):
						arguments[temp_arg] = str(doc[doc_index])
				else:
					detection_index = 0
					going_through_construction = False
					detection_text_idx_start = -1

			elif(pair_to_check[1] == 4): # CHECK LEMMA
				if(check(rule_token, str(doc[doc_index].lemma_))):
					detection_index += 1
					if(not going_through_construction):
						detection_text_idx_start = doc[doc_index].idx
						going_through_construction = True

					if(has_arg):
						arguments[temp_arg] = str(doc[doc_index])
				else:
					detection_index = 0
					going_through_construction = False
					detection_text_idx_start = -1

			elif(pair_to_check[1] == 2): # CHECK OPTIONAL STRING
				if(check(rule_token, str(doc[doc_index]))):
					detection_index += 1
					if(not going_through_construction):
						detection_text_idx_start = doc[doc_index].idx
						going_through_construction = True

					if(has_arg):
						arguments[temp_arg] = str(doc[doc_index])
				else:
					arguments[temp_arg] = ''
					detection_index += 1
					doc_index -= 1

			elif(pair_to_check[1] == 3): # CHECK OPTIONAL POS TAG
				if(check(rule_token, str(doc[doc_index].tag_))):
					detection_index += 1
					if(not going_through_construction):
						detection_text_idx_start = doc[doc_index].idx
						going_through_construction = True

					if(has_arg):
						arguments[temp_arg] = str(doc[doc_index])
				else:
					arguments[temp_arg] = ''
					detection_index += 1
					doc_index -= 1

			elif(pair_to_check[1] == 5): # CHECK OPTIONAL LEMMA
				if(check(rule_token, str(doc[doc_index].lemma_))):
					detection_index += 1
					if(not going_through_construction):
						detection_text_idx_start = doc[doc_index].idx
						going_through_construction = True

					if(has_arg):
						arguments[temp_arg] = str(doc[doc_index])
				else:
					arguments[temp_arg] = ''
					detection_index += 1
					doc_index -= 1


			if(detection_index >= len(detection_pattern)): # Check if full pattern detected
				detection_flag = True

				going_through_construction = False
				detection_text_idx_end = doc[doc_index].idx + len(doc[doc_index]) # Get end offset id of detected construction

				output_parts.append(doc.text[get_input_text_idx_start:detection_text_idx_start]) # All text before the detected construction started
				get_input_text_idx_start = detection_text_idx_end

				replacement_part = []

				for rep_token in replacement_pattern: #Add replacement construction to output
					if(rep_token[0] == "[" and rep_token[1] == "@" and rep_token[-1] == "]"):
						arg_to_get = rep_token[2]
						output_rep_token = arguments[arg_to_get] # Default output

						if(output_rep_token == ''): # If it's empty, skip loop iteration
							continue

						if(rep_token[3] == ":"): # Default replacement provided

							add_maps = rep_token[4:-1].split("|")

							repl_flag = False
							for i in add_maps[1:]:
								i_temp = i.split(":")
								if(output_rep_token == i_temp[0]):
									output_rep_token = i_temp[1] # Making the replacement
									repl_flag = True
									break

							if(not repl_flag):
								output_rep_token = add_maps[0]

						elif(rep_token[3] == "|"): # Additional replacements provided
							
							add_maps = rep_token[4:-1].split("|")

							for i in add_maps:
								i_temp = i.split(":")
								if(output_rep_token == i_temp[0]):
									output_rep_token = i_temp[1] # Making the replacement
									break

						replacement_part.append(output_rep_token)

					else:
						replacement_part.append(rep_token)

				output_parts.append(" ".join(replacement_part))
				detection_index = 0

			doc_index += 1


		if(detection_flag):
			output_parts.append(doc.text[get_input_text_idx_start:])

			text = "".join(output_parts)
			construction_detected_in_line = True

	#if(construction_detected_in_line):
	#	print("Construct Detected\t" + text)
	#else:
	#	print("Not Detected\t" + text)

	#Output after applying all rules
	print(text)

