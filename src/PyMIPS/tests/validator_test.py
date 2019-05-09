from PyMIPS.Datastructure.instruction_types import IType, RType, JType
from PyMIPS.AST.validator import validate
import unittest


class TestRType(unittest.TestCase):
    def test_all(self):
        try:
            RType("add", "$t3", "$t2", "$t1")
            RType("addu", "$t3", "$t2", "$t1")
            RType("and", "$t3", "$t2", "$t1")
            RType("nor", "$t3", "$t2", "$t1")
            RType("or", "$t3", "$t2", "$t1")
            RType("sll", "$t3", "$t2", "$t1")
            RType("slt", "$t3", "$t2", "$t1")
            RType("sltu", "$t3", "$t2", "$t1")
            RType("sra", "$t3", "$t2", "$t1")
            RType("srav", "$t3", "$t2", "$t1")
            RType("sub", "$t3", "$t2", "$t1")
            RType("subu", "$t3", "$t2", "$t1")
            RType("xor", "$t3", "$t2", "$t1")
            RType("div", "$t3", "$t2")
            RType("divu", "$t3", "$t2")
            RType("jalr", "$t3", "$t2")
            RType("mult", "$t3", "$t2")
            RType("multu", "$t3", "$t2")
            RType("move", "$t3", "$t2")
            RType("mfhi", "$t3")
            RType("mflo", "$t3")
            RType("mthi", "$t3")
            RType("mtlo", "$t3")
            RType("syscall", destination=None)
        except:
            self.fail()

    def test_bad_3(self):
        with self.assertRaises(Exception):
            RType("add", "$t3")
        with self.assertRaises(Exception):
            RType("sub", "$t3", "4")
        with self.assertRaises(Exception):
            RType("move", "$3", "t435", "$vew")
        with self.assertRaises(Exception):
            RType("lw", "$t3", "$s4", "gfd4")
        with self.assertRaises(Exception):
            RType("", "$t3")

    def test_bad_2(self):
        with self.assertRaises(Exception):
            RType("add", "$t3", "$t4")
        with self.assertRaises(Exception):
            RType("div", "$t3")
        with self.assertRaises(Exception):
            RType("mul", "$t3", "4")
        with self.assertRaises(Exception):
            RType("jalr", "$t3")

    def test_bad_1(self):
        with self.assertRaises(Exception):
            RType("mfhi", "$t3", "$t4")
        with self.assertRaises(Exception):
            RType("mflo")


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
