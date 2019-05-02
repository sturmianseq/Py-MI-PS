class Register:
    def __init__(self, name):
        self.name = name
        self.__contents = lambda: 0

    def __repr__(self):
        return f"Register({self.name}, {str(self.__contents())})"

    def set_contents(self, value):
        self.__contents = value

    def get_contents(self):
        return self.__contents()


class RegisterPool:
    """RegisterPool is a collection of static methods that handle register interactions
    """

    __registers = {"$zero": Register("$zero")}

    @staticmethod
    def print_all_active_registers():
        for key in RegisterPool.__registers:
            print(RegisterPool.__registers[key])

    @staticmethod
    def get_register(name: str) -> Register:
        if name in RegisterPool.__registers.keys():
            return RegisterPool.__registers[name]
        else:
            reg = Register(name)
            RegisterPool.__registers[name] = reg
            return reg

