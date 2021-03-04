import googletrans
import sys
import time
from googletrans import Translator

if(len(sys.argv) < 4):
	print("Not enough arguments.")
	sys.exit()

translator = Translator()
source_language = 'en'
destination_language = 'hi'

source_input = sys.argv[1]

replace_source = sys.argv[2]
replace_target = sys.argv[3]

print("Original Input: " + source_input)
result_original = translator.translate(source_input, src=source_language, dest=destination_language)
print("Original Translation: " + result_original.text)

print("\nPre-processing: " + replace_source + " -> " + replace_target)
time.sleep(2.5)
preprocessed_input = source_input.replace(replace_source, replace_target)
print("\nPre-processed input: " + preprocessed_input)

time.sleep(2.5)

result_final = translator.translate(preprocessed_input, src=source_language, dest=destination_language)
print("Final Translation: " + result_final.text)
