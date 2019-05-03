from PyMIPS.Datastructure.register import RegisterPool
from PyMIPS.Datastructure.data_model import data_stack


def run_from_list(commands: list):
    try:

        iteration = 0
        for c in commands:
            print(f"({iteration}): {str(c)}")
            c()
            RegisterPool.print_all_active_registers()
            print()
            # heap.print_all_active_refs()
            # print()
            data_stack.print_stack()
            iteration += 1
    except:
        return False

    return True
