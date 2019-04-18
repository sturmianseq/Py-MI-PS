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
    # Basic Instructions
    r"li",
    r"la",
    r"add",
    r"addi",
    r"addiu",
    r"addu",
    r"and",
    r"andi",
    r"beq",
    r"bgez",
    r"bgezal",
    r"bgtz",
    r"blez",
    r"bltz",
    r"bltzal",
    r"bne",
    r"break",
    r"div",
    r"divu",
    r"eret",
    r"j",
    r"jal",
    r"jalr",
    r"jr",
    r"lb",
    r"lbu",
    r"lh",
    r"lhu",
    r"ll",
    r"lui",
    r"lw",
    r"lwl",
    r"lwr",
    r"madd",
    r"maddu",
    r"mfhi",
    r"mflo",
    r"move",
    r"msub",
    r"msubu",
    r"mthi",
    r"mtlo",
    r"mul",
    r"mult",
    r"nop",
    r"nor",
    r"or",
    r"ori",
    r"sb",
    r"sc",
    r"sh",
    r"sll",
    r"sllv",
    r"slt",
    r"slti",
    r"sltiu",
    r"sltu",
    r"sra",
    r"srav",
    r"srl",
    r"srlv",
    r"sub",
    r"subu",
    r"sw",
    r"swl",
    r"slr",
    r"syscall",
    r"teq",
    r"teqi",
    r"tge",
    r"tgei",
    r"tgeiu",
    r"tgeu",
    r"tlt",
    r"tlti",
    r"tltiu",
    r"tltu",
    r"tne",
    r"tnei",
    r"xor",
    r"xori",
    r"abs",
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
