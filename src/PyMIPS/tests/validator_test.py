from PyMIPS.Datastructure.instruction_types import IType, RType, JType
import unittest


def test_correct_rtype():
    RType("add", "$t4", "$t2", "$t3")

