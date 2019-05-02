from PyMIPS.Datastructure.immediate import Immediate, Ref_Immediate
from PyMIPS.Datastructure.register import RegisterPool, Register

rp = RegisterPool


def create_immediate(value) -> Immediate:
    if type(value) == int:
        return Immediate(lambda: value)
    if type(value) == str:
        return Ref_Immediate(value)
    return None


def create_register(value) -> Register:
    if value is None:
        return None
    return rp.get_register(value)
