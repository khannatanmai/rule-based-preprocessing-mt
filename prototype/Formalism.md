# Source side rules
- `[...]` : POS Tags
- `[..@1]` : Arguments numbered `0-9,a-z`,etc. to be used in the target side

# Target side rules
- `[@1]` : Add the argument numbered 1 in the target side construction

# General
- `|` used as OR, can be used for POS tags or strings
- Anything not in `[...]` is matched directly