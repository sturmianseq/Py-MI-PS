import sys

from PyMIPS.lexer import lex
from PyMIPS.AST.ast import parse
from PyMIPS.tests.classes_test import example1_test

if __name__ == "__main__":
    """
    filename = sys.argv[1]
    with open(filename) as file:
        characters = file.read()
    tokens = lex(characters)
    print(tokens)
    print("\n\n")
    res = parse(tokens)
    print(res)
    """
    example1_test()

