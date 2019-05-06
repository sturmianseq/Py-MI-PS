from PyMIPS.Datastructure.instruction_types import IType, RType, JType


def validate(instruction) -> bool:
    """[summary]
    
    Parameters
    ----------
    instruction : [type]
        [description]
    
    Returns
    -------
    bool
        [description]
    """
    switch = {
        "li": validate_li,
        "sw": validate_sw,
        "add": validate_3_rtype,
        "sub": validate_3_rtype,
    }
    try:
        func = switch[instruction.command]
        res = func(instruction)
    except:
        res = False
    return res


def validate_3_rtype(instruction) -> bool:
    rd = instruction.destination
    rs = instruction.source_register
    rt = instruction.target_register

    check1 = rd is not None
    check2 = rs is not None
    check3 = rt is not None

    return check1 and check2 and check3


def validate_2_rtype(instruction) -> bool:
    rd = instruction.destination
    rs = instruction.r1
    rt = instruction.r2

    check1 = rd is None
    check2 = rs is not None
    check3 = rt is not None

    return check1 and check2 and check3


def validate_li(instruction) -> bool:
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
