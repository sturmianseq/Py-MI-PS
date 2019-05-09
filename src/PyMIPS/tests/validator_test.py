from PyMIPS.Datastructure.instruction_types import IType, RType, JType
from PyMIPS.AST.validator import validate
import unittest


class TestRType(unittest.TestCase):
    def test_3(self):
        try:
            RType("add", "$t3", "$t2", "$t1")
        except:
            self.fail()

    def test_bad_3(self):
        with self.assertRaises(Exception):
            RType("add", "$t3")


class TestIType(unittest.TestCase):
    def test_3(self):
        try:
            IType("lw", "$t0", 4, "$sp")
        except:
            self.fail()

    def test_bad_3(self):
        with self.assertRaises(Exception):
            IType("lw", "$t0", immediate=None)
        with self.assertRaises(Exception):
            IType("add", "$t32")
        with self.assertRaises(Exception):
            IType("lw", "t32", immediate=None)

    def test_2(self):
        try:
            IType("li", "$t0", 4)
            IType("sw", "$t0", -4, "$sp")
        except:
            self.fail()

    def test_bad_2(self):
        with self.assertRaises(Exception):
            IType("li", "$t3", source="$t2")
        with self.assertRaises(Exception):
            IType("li", source="$t2")
