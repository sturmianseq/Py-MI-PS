class Register:
    def __init__(self, name):
        self.name = name
        self.__contents = 0

    def __repr__(self):
        return f"Register({self.name}, {str(self.__contents)})"

    def set_contents(self, value):
        self.__contents = value

    def get_contents(self):
        return self.__contents


class RegisterPool:
    __instance = None

    @staticmethod
    def get_instance():
        if RegisterPool.__instance == None:
            RegisterPool()
        return RegisterPool.__instance

    def __init__(self):
        if RegisterPool.__instance != None:
            raise Exception("Cannot instantiate")
        else:
            RegisterPool.__instance = self
            self.registers = {"$zero": Register("$zero")}

    def get_register(self, name) -> Register:
        if name in self.registers.keys():
            return self.registers[name]
        else:
            reg = Register(name)
            self.registers[name] = reg
            return reg

