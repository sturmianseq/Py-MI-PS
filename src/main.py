from PyMIPS.lexer import *
from PyMIPS.parser import prepare
from PyMIPS.ast import parser

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as file:
        characters = file.read()
    tokens = lex(characters)
    print(str(tokens) + "\n\n")
    result = prepare(tokens)
    print(str(result) + "\n\n")
    ast = parser()(tokens, 0)
    print(ast)

