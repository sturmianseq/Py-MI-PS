import sys
import re

NEWLINE = "NEWLINE"
DIRECTIVE = "DIRECTIVE"
LABEL = "LABEL"
COMMAND = "COMMAND"
REGISTER = "REGISTER"
REFERENCE = "REFERENCE"
INT = "INT"
SEPERATOR = "SEPERATOR"
STRING = "STRING"

commands = [
    r"li",
    r"lw",
    r"add",
    r"sub",
    r"sw",
    r"syscall",
    r"la",
    r"move",
    r"addi",
    r"addiu",
    r"addu",
    r"and",
    r"andi",
    r"bc1f",
    r"bc1t",
    r"",
]
registers = [r"[$][^\s,]+"]


token_exprs = (
    [
        (r"[\n\r]+", None),
        (r"[\s]+", None),
        (r"[#]+[^\n]+", None),
        (r"[.][^\s\n]+", DIRECTIVE),
        (r"[^\s]+[:]", LABEL),
        (r'".+"', STRING),
    ]
    + [(c, COMMAND) for c in commands]
    + [(r"[,]", SEPERATOR)]
    + [(r, REGISTER) for r in registers]
    + [(r"[0-9]+", INT), (r"[A-Za-z][A-Za-z0-9_]*", REFERENCE)]
)


def lex(characters):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write(f"Illegal character at pos {pos}: {characters[pos]}\n")
            print(characters[pos - 5 : pos + 5])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens
