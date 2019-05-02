from PyMIPS.Datastructure.emulator import data_stack, register_pool, heap


def run_from_list(commands: list):
    iteration = 0
    for c in commands:
        print(f"({iteration}): {str(c)}")
        c()
        register_pool.print_all_active_registers()
        print()
        heap.print_all_active_refs()
        print()
        data_stack.print_stack()
        iteration += 1
