from PyMIPS.AST.classes import I_Type, R_Type, J_Type
from PyMIPS.Datastructure.execution_stack import run_from_list
from PyMIPS.Datastructure.immediate import StoredRefs


def example1_test():
    exe = [0, 1, 2, 3, 4, 5]
    StoredRefs.store_ref("value", lambda: 12)
    StoredRefs.store_ref("Z", lambda: 0)
    exe[0] = I_Type("li", "$t2", immediate=25)
    exe[1] = I_Type("lw", "$t3", immediate="value")
    exe[2] = R_Type("add", "$t4", "$t2", "$t3")
    exe[3] = R_Type("sub", "$t5", "$t2", "$t3")
    exe[4] = I_Type("sw", "$t2", immediate="Z")
    exe[5] = I_Type("sw", "$t5", "$sp", 4)
    run_from_list(exe)
