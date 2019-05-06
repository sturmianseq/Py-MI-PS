from PyMIPS.Datastructure.instruction_types import IType, RType, JType
from PyMIPS.Datastructure.execution_stack import run_from_list
from PyMIPS.Datastructure.data_model import DataHeap, DataStack


def test_example1():
    DataStack.alloc(1024)
    DataHeap.alloc(1024)
    DataHeap.store(12, "value")
    DataHeap.store(0, "Z")
    exe = [0, 1, 2, 3, 4, 5]
    exe[0] = IType("li", "$t2", 25)
    exe[1] = IType("lw", "$t3", "value")
    exe[2] = RType("add", "$t4", "$t2", "$t3")
    exe[3] = RType("sub", "$t5", "$t2", "$t3")
    exe[4] = IType("sw", "$t5", "Z")
    exe[5] = IType("sw", "$t4", 4, "$sp")
    assert run_from_list(exe) == True
