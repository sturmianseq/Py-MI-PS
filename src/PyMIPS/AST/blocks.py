class Globl:
    def __init__(self, entry):
        self.entry = entry

    def __repr__(self):
        return f"Entry Point: {self.entry}"


class TextBlock:
    def __init__(self, contents):
        self.contents = unpack(contents)

    def __repr__(self):
        c = ""
        for item in self.contents:
            c += str(item) + "\n"

        return f"Text Block:\n{c}"


class DataBlock:
    def __init__(self, contents):
        self.contents = unpack(contents)

    def __repr__(self):
        c = ""
        for item in self.contents:
            c += "\t" + str(item) + "\n"
        return f"Data Block:\n{c}"


class Label:
    def __init__(self, name, contents):
        self.name = name
        self.contents = unpack(contents)

    def __repr__(self):
        c = ""
        for item in self.contents:
            c += "\t" + str(item) + "\n"
        return f"{self.name}\n{str(c)}"


class Program:
    def __init__(self, contents):
        self.contents = unpack(contents)

    def __repr__(self):
        c = ""
        for item in self.contents:
            c += str(item)
        return f"Program:\n\n{c}"


def unpack(contents: tuple) -> list:
    result = []
    while type(contents) == tuple:
        value, contents = contents
        result.append(value)
    result.append(contents)
    return result

