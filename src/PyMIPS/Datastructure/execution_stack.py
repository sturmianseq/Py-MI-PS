from PyMIPS.Datastructure.data_model import RegisterPool, DataStack, DataHeap
from PyMIPS.Datastructure.memory import Memory


def run_from_list(commands: list):

    iteration = 0
    for c in commands:
        print(f"({iteration}): {str(c)}")
        c()
        print()
        iteration += 1
    return True

