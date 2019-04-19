import sys

from PyMIPS.lexer import lex

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as file:
        characters = file.read()
    tokens = lex(characters)
    print(tokens)

