# Rule-based pre-processing of non-compositional constructions to simplify them and improve black-box machine translation

## How to Use
- Install dependencies using `pip install -r requirements.txt`
- `python3 src/preprocess.py [input sentence] [rule-set.ppr]`
- Test using `./tests/test.sh`

## External tools used
- spacy POS tagger
- Download model using `python -m spacy download en_core_web_sm`

## Rule formalism (File extension .ppr)

### Source side rules
- `[...]` : POS Tags
- `[..@1]` : Variables named `0-9,a-z`,etc. to be used in the target side
- `|` used as OR, can be used for POS tags or strings
- `(...)` : Optional tokens, can be used on both POS tags or strings, i.e. `(not)` or `([NN])`
- `!` used as NOT, can be used for POS tags `[!...]` or strings `!xyz`
- If you just want to define the context, use variables to copy the context over to the target.

For example, if you want a rule that matches "the" followed by an Adjective, which is NOT followed by a noun, it will look something like: ```the [JJ@1] [!NN|NNS@2] -> [@1] people [@2]```

### Target side rules
- `[@1]` : Add the variable named 1 in the target side construction

### General

- Anything not in `[...]` is matched directly
- Rules are put in a list and applied on the input sentence one after the other.
- Only lines with `->` in the rule-set are counted as rules.
