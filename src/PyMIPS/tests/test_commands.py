try:
    from src.PyMIPS.Datastructure.memory import Memory
    from src.PyMIPS.Datastructure.instruction_types import IType, JType, RType
    from src.PyMIPS.Datastructure.data_model import RegisterPool
except:
    from PyMIPS.Datastructure.memory import Memory
    from PyMIPS.Datastructure.data_model import RegisterPool
    from PyMIPS.Datastructure.instruction_types import IType, JType, RType

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
        pass

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
        i = IType("sll", "$t0", "$t1", 2)
        t0 = RegisterPool.get_register("$t0")
        t1 = RegisterPool.get_register("$t1")
        t1.set_contents_from_int(4)
        i()
        self.assertEqual(t0.get_contents_as_int(), 16)

    def test_srl(self):
        # TODO: srl
        return

    def test_sra(self):
        # TODO: sra
        return

    def test_beq(self):
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
        pass

    def test_lbu(self):
        pass

    def test_sb(self):
        pass

    def test_sh(self):
        pass

    def test_sw(self):
        pass
