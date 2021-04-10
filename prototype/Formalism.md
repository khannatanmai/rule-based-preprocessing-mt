# Source side rules
- `[...]` : POS Tags
- `[..@1]` : Arguments numbered `0-9,a-z`,etc. to be used in the target side
- `|` used as OR, can be used for POS tags or strings

# Target side rules
- `[@1]` : Add the argument numbered 1 in the target side construction

# General

- Anything not in `[...]` is matched directly
- Rules are put in a list and applied on the input sentence one after the other.
- Only lines with `->` in the rule-set are counted as rules.