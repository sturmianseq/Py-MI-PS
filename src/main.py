import sys

from PyMIPS.lexer import lex
from PyMIPS.AST.ast import parser

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as file:
        characters = file.read()
    tokens = lex(characters)
    print(tokens)
    print("\n\n")
    ast = parser()(tokens, 0)
    print(ast)

