from PyMIPS.Datastructure.data_model import RegisterPool, DataStack, DataHeap
from PyMIPS.Datastructure.memory import Memory


def run_from_list(commands: list):

    try:
        iteration = 0
        for c in commands:
            print(f"({iteration}): {str(c)}")
            c()
            RegisterPool.print_all_active_registers()
            print()
            DataHeap.print()
            Memory.print()
            iteration += 1
        return True
    except:
        return False

