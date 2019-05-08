import sys

from PyMIPS.tests.example1_test import test_example1
from PyMIPS.Datastructure.memory import Memory

if __name__ == "__main__":
    """
    filename = sys.argv[1]
    with open(filename) as file:
        characters = file.read()
    tokens = lex(characters)
    #print(tokens)
    #print("\n\n")
    res = parse(tokens)
    print(res)
    """
    test_example1()
    # Memory.store_asciiz("Storing data is fun", 2014)
    # Memory.print()
    # print(Memory.load_asciiz(2014))
