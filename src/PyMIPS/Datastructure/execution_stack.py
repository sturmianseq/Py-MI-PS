from PyMIPS.Datastructure.register import RegisterPool

class ExecutionStack:
    def __init__(self):
        rp = RegisterPool.get_instance()
        self.pc = rp.get_register("$pc")
        self.stack = []
    
    def add_instruction(self, instruction):


    def execute_next(self):
