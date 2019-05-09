import sys

from PyMIPS.lexer import lex
from PyMIPS.AST.ast import parse
from PyMIPS.Datastructure.execution_stack import run_program

if __name__ == "__main__":

    filename = sys.argv[1]
    with open(filename) as file:
        characters = file.read()
    tokens = lex(characters)
    res = parse(tokens)
    run_program(res.value)

