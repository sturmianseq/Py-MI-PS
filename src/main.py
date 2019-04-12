from PyMIPS.lexer import *
from PyMIPS.parser import parse

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as file:
        characters = file.read()
    tokens = lex(characters)
    result = parse(tokens)
    for r in result:
        print(r)

