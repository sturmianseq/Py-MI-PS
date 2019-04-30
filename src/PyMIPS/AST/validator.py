def validate(instruction) -> bool:
    switch = {
        "li": validate_li,
        "sw": validate_sw,
        "add": validate_add,
        "add": validate_3_rtype,
        "sub": validate_3_rtype,
    }
    func = switch[instruction.command]
    try:
        res = func(instruction)
    except:
        res = False
    return res


def validate_3_rtype(instruction):
    return True


def validate_li(instruction):
    target = instruction.target_register
    source = instruction.source_register
    immediate = instruction.immediate

    check1 = target is not None
    check2 = source is None
    check3 = immediate is not None

    return check1 and check2 and check3


def validate_sw(instruction):
    return True


def validate_add(instruction):
    return True
