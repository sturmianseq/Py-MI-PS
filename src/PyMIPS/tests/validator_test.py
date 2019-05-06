from PyMIPS.Datastructure.instruction_types import IType, RType, JType
from PyMIPS.AST.validator import validate
import unittest


def test_correct_rtype():
    rtype_test = RType("add", "$t4", "$t2", "$t3")
    assert validate(rtype_test) == True

def test_incorrect_rtype():
    rtype_test = RType("li", "$t4", "$t2", "$t3")
    assert validate(rtype_test) == False