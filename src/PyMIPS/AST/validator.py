def validate(instruction) -> bool:
    """Validates an instruction
    
    Parameters
    ----------
    instruction : BaseCommand
        The instruction to validate
    
    Returns
    -------
    bool
        Valid or not valid
    """
    switch = {
        "lw": validate_optional_2_type,
        "li": validate_1_itype,
        "sw": validate_optional_2_type,
        "add": validate_3_rtype,
        "sub": validate_3_rtype,
        "div": validate_2_rtype,
        "move": validate_2_rtype,
    }
    try:
        func = switch[instruction.command]
        res = func(instruction)
    except:
        res = False
    return res


def validate_3_rtype(instruction) -> bool:
    rd = instruction.destination_register
    rs = instruction.source_register
    rt = instruction.target_register

    check1 = rd is not None
    check2 = rs is not None
    check3 = rt is not None

    return check1 and check2 and check3


def validate_2_rtype(instruction) -> bool:
    rd = instruction.destination_register
    rs = instruction.source_register
    rt = instruction.target_register

    check1 = rd is not None
    check2 = rs is not None
    check3 = rt is None

    return check1 and check2 and check3


def validate_1_rtype(instruction) -> bool:
    rd = instruction.destination_register
    rs = instruction.source_register
    rt = instruction.target_register

    check1 = rd is not None
    check2 = rs is None
    check3 = rt is None

    return check1 and check2 and check3


def validate_2_itype(instruction) -> bool:
    destination = instruction.destination_register
    source = instruction.source_register
    target = instruction.target_register
    immediate = instruction.immediate

    check1 = destination is not None
    check2 = source is not None
    check3 = immediate is not None
    check4 = target is None
    print(check1, check2, check3, check4)

    return check1 and check2 and check3 and check4


def validate_optional_2_type(instruction) -> bool:
    destination = instruction.destination_register
    source = instruction.source_register
    target = instruction.target_register
    immediate = instruction.immediate

    check1 = destination is not None
    check2 = source is not None or None
    check3 = immediate is not None
    check4 = target is None
    print(check1, check2, check3, check4)

    return check1 and check2 and check3 and check4


def validate_1_itype(instruction) -> bool:
    destination = instruction.destination_register
    target = instruction.target_register
    immediate = instruction.immediate
    source = instruction.source_register

    check1 = destination is not None
    check2 = target is None
    check3 = immediate is not None
    check4 = source is None
    print(check1, check2, check3, check4)

    return check1 and check2 and check3 and check4

