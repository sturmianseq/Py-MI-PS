try:
    from src.PyMIPS.Datastructure.memory import Memory
    from src.PyMIPS.Datastructure.instruction_types import (
        IType,
        JType,
        RType,
        BaseCommand,
        DataStack,
        DataHeap,
    )

    from src.PyMIPS.Datastructure.data_model import RegisterPool, ProgramStack
except:
    from PyMIPS.Datastructure.memory import Memory
    from PyMIPS.Datastructure.data_model import (
        RegisterPool,
        ProgramStack,
        DataStack,
        DataHeap,
    )
    from PyMIPS.Datastructure.instruction_types import IType, JType, RType, BaseCommand

import unittest

"""
sll, srl, and sra are treated as I Types
"""


class TestRTypes(unittest.TestCase):
    def test_sllv(self):
        # TODO: sllv
        return

    def test_srlv(self):
        # TODO: srlv
        return

    def test_srav(self):
        # TODO: srav
        return

    def test_jr(self):
        pass

    def test_jalr(self):
        pass

    def test_jalr_2_r(self):
        pass

    def test_syscall(self):
        pass

    def test_mfhi(self):
        pass

    def test_mthi(self):
        pass

    def test_mflo(self):
        pass

    def test_mtlo(self):
        pass

    def test_mult(self):
        pass

    def test_multu(self):
        pass

    def test_div(self):
        pass

    def test_divu(self):
        pass

    def test_add(self):
        r = RType("add", "$t0", "$t1", "$t3")
        t0 = RegisterPool.get_register("$t0")
        t1 = RegisterPool.get_register("$t1")
        t3 = RegisterPool.get_register("$t3")
        t1.set_contents_from_int(4)
        t3.set_contents_from_int(6)
        r()
        self.assertEqual(t0.get_contents_as_int(), 10)

    def test_addu(self):
        pass

    def test_sub(self):
        pass

    def test_subu(self):
        pass

    def test_and(self):
        pass

    def test_or(self):
        pass

    def test_xor(self):
        pass

    def test_nor(self):
        pass

    def test_slt(self):
        pass

    def test_sltu(self):
        pass


class TestJTypes(unittest.TestCase):
    pass


class TestITypes(unittest.TestCase):
    def test_sll(self):
        # TODO: sll
        i = IType("sll", "$t0", 2, "$t1")
        t0 = RegisterPool.get_register("$t0")
        t1 = RegisterPool.get_register("$t1")
        t1.set_contents_from_int(4)
        i()
        # changed from 16 to 20 to test i-types that I am doing
        self.assertEqual(t0.get_contents_as_int(), 16)

    def test_srl(self):
        # TODO: srl
        return

    def test_sra(self):
        # TODO: sra
        return

    def test_beq(self):
        # TODO: ashton
        return

    def test_bne(self):
        pass

    def test_blez(self):
        pass

    def test_bgtz(self):
        pass

    def test_addi(self):
        i = IType("addi", "$t0", immediate=10, source="$t1")
        t0 = RegisterPool.get_register("$t0")
        t1 = RegisterPool.get_register("$t1")
        t1.set_contents_from_int(10)
        i()
        self.assertEqual(t0.get_contents_as_int(), 20)

    def test_addiu(self):
        pass

    def test_slti(self):
        pass

    def test_sltiu(self):
        pass

    def test_andi(self):
        # i = IType("andi", "t0", 1, "$t1")
        # t0 = RegisterPool.get_register("t0")
        # t1 = RegisterPool.get_register("$t1")
        # t1.set_contents_from_bytes(1)
        pass

    def test_ori(self):
        pass

    def test_xori(self):
        pass

    def test_lui(self):
        pass

    def test_lb(self):
        pass

    def test_lh(self):
        pass

    def test_lw(self):
        Memory.reset()
        DataStack.alloc(1024)
        DataStack.store_word(4, 1203)
        i = IType("lw", "$t0", 4, source="$sp")
        t0 = RegisterPool.get_register("$t0")
        i()
        self.assertEqual(t0.get_contents_as_int(), 1203)

    def test_lbu(self):
        pass

    def test_sb(self):
        pass

    def test_sh(self):
        pass

    def test_sw_stack(self):
        Memory.reset()
        # sw $t0, 4($sp)
        DataStack.alloc(1024)
        i = IType("sw", "$t0", 4, "$sp")
        t0 = RegisterPool.get_register("$t0")
        t0.set_contents_from_int(673)
        i()
        self.assertEqual(DataStack.load_word(4, "$sp"), 673)

    def test_sw_heap(self):
        Memory.reset()
        DataHeap.reset()
        DataHeap.alloc(1024)
        DataHeap.store_word(218, "data")
        i = IType("sw", "$t0", "data")
        t0 = RegisterPool.get_register("$t0")
        t0.set_contents_from_int(1999)
        i()
        self.assertEqual(DataHeap.get_value_as_int("data"), 1999)
