from PyMIPS.Datastructure.instruction_types import IType, RType, JType
from PyMIPS.AST.validator import validate
import unittest


def test_correct_3rtype():
    rtype_test = RType("add", "$t4", "$t2", "$t3")
    assert validate(rtype_test) == True


def test_incorrect_3rtype():
    rtype_test = RType("li", "$t4", "$t2", "$t3")
    assert validate(rtype_test) == False


def test_correct_2rtype():
    r_test = RType("div", "$t4", "$t2")
    assert validate(r_test) == True
