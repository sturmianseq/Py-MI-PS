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
PAREN = "PAREN"
STRING = "STRING"

commands = [
    # Basic Instructions
    r"syscall",
    r"bgezal",
    r"bltzal",
    r"addiu",
    r"break",
    r"maddu",
    r"msubu",
    r"sltiu",
    r"tgeiu",
    r"tltiu",
    r"addi",
    r"addu",
    r"andi",
    r"bgez",
    r"bgtz",
    r"blez",
    r"bltz",
    r"divu",
    r"eret",
    r"jalr",
    r"madd",
    r"mfhi",
    r"mflo",
    r"move",
    r"msub",
    r"mthi",
    r"mtlo",
    r"mult",
    r"sllv",
    r"slti",
    r"sltu",
    r"srav",
    r"srlv",
    r"subu",
    r"teqi",
    r"tgei",
    r"tgeu",
    r"tlti",
    r"tltu",
    r"tnei",
    r"xori",
    r"add",
    r"and",
    r"beq",
    r"bne",
    r"div",
    r"jal",
    r"lbu",
    r"lhu",
    r"lui",
    r"lwl",
    r"lwr",
    r"mul",
    r"nop",
    r"nor",
    r"ori",
    r"sll",
    r"slt",
    r"sra",
    r"srl",
    r"sub",
    r"swl",
    r"slr",
    r"teq",
    r"tge",
    r"tlt",
    r"tne",
    r"xor",
    r"abs",
    r"la",
    r"jr",
    r"lb",
    r"lh",
    r"ll",
    r"lw",
    r"or",
    r"sb",
    r"sc",
    r"sh",
    r"sw",
    r"j",
    r"li",
]
registers = [r"[$][^\s,)]+"]


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
    + [(r"[()]", PAREN)]
    + [(r, REGISTER) for r in registers]
    + [(r"[+-]?\d+", INT), (r"[A-Za-z][A-Za-z0-9_]*", REFERENCE)]
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
