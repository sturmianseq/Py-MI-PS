import sys

from PyMIPS.tests.validator_test import test_correct_rtype, test_incorrect_rtype

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
    test_correct_rtype()
    test_incorrect_rtype()

