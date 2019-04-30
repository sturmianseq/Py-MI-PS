from PyMIPS.Datastructure.register import RegisterPool
from PyMIPS.Datastructure.immediate import StoredRefs
from PyMIPS.Datastructure.commands import data_stack

rp = RegisterPool.get_instance()


def run_from_list(commands: list):
    iteration = 0
    for c in commands:
        print(f"({iteration}): {str(c)}")
        c()
        rp.print_all_active_registers()
        print()
        StoredRefs.print_all_active_refs()
        print()
        data_stack.print_stack()
        iteration += 1
