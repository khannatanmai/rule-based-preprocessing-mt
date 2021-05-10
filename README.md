# Rule-based pre-processing of non-compositional constructions to simplify them and improve black-box machine translation

## Purpose
This rule-based pre-processor is used to detect non-compositional constructions in text using rules and pre-process them into more compositional but still equivalent constructions such that the machine translation of the input text improves significantly.

## How to Use
- Install dependencies using `pip install -r requirements.txt`
- Download spacy model using `python -m spacy download en_core_web_sm`
- `python3 src/preprocess.py [rule_file.ppr] [input_file.txt]`
- Test using `./tests/test.sh`

Note: This assumes your input is already sentence tokenised. If it's not, you can use the `spacy` sentence tokeniser first.

## Rule formalism (File extension .ppr)

## **Sample rule file: `tests/rulesets/eng-hin.ppr`**

### Source side rules
- `[...]` : POS Tags
- `[..@1]` : Variables named `0-9,a-z`,etc. to be used in the target side
- `|` used as OR, can be used for POS tags or strings
- `(...)` : Optional tokens, can be used on both POS tags or strings, i.e. `(not)` or `([NN])`
- `!` : Used as NOT, can be used for POS tags `[!...]` or strings `!xyz`
- `[] or [@1]` : Will match any token
- If you just want to define the context, use variables to copy the context over to the target.

For example, if you want a rule that matches "the" followed by an Adjective, which is NOT followed by a noun, it will look something like: ```the [JJ@1] [!NN|NNS@2] -> [@1] people [@2]```

### Target side rules
- `[@1]` : Add the variable named 1 in the target side construction
- `[@2|my:me|his:him]` : Add any number of mappings in the target side. If the string in the variable matches the left side of any of `:` separated strings, the right side will appear in the output. Can be used to hardcode morph changes, etc.
- `[@1:die|kick:die|kicks:dies]` : The user can also define a default replacement of the token, in case none of the maps defined execute. If no default value is defined, and none of the maps execute, then the value in the variable is printed out.

### General

- Anything not in `[...]` is matched directly
- Rules are put in a list and applied on the input sentence one after the other.
- Only lines with `->` in the rule-set are counted as rules.

## Testing
- Run tests using `tests/test.sh`

## Miscellaneous Information
This project is part of my Master's thesis in Computational Linguistics at IIIT Hyderabad titled: **Rule-based pre-processing of idioms and non-compositional constructions to simplify them and improve black-box machine translation**, done under the guidance of my advisor Dr. Dipti Sharma.

You can open an issue on this repo to report any bugs or just to ask a doubt.
