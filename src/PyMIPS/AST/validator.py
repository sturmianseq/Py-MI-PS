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
        # R Type instructions
        "add": validate_3_rtype,
        "addu": validate_3_rtype,
        "and": validate_3_rtype,
        "nor": validate_3_rtype,
        "or": validate_3_rtype,
        "sll": validate_3_rtype,
        "sllv": validate_3_rtype,
        "slt": validate_3_rtype,
        "sltu": validate_3_rtype,
        "sra": validate_3_rtype,
        "srav": validate_3_rtype,
        "srl": validate_3_rtype,
        "srlv": validate_3_rtype,
        "sub": validate_3_rtype,
        "subu": validate_3_rtype,
        "xor": validate_3_rtype,
        "div": validate_2_rtype,
        "divu": validate_2_rtype,
        "jalr": validate_2_rtype,
        "mult": validate_2_rtype,
        "multu": validate_2_rtype,
        "move": validate_2_rtype,
        "jr": validate_1_rtype,
        "mfhi": validate_1_rtype,
        "mflo": validate_1_rtype,
        "mthi": validate_1_rtype,
        "mtlo": validate_1_rtype,
        "syscall": validate_0_rtype,
        # I Type instructions
        "addi": validate_2_itype,
        "addiu": validate_2_itype,
        "andi": validate_2_itype,
        "beq": validate_2_itype,
        "bne": validate_2_itype,
        "ori": validate_2_itype,
        "slti": validate_2_itype,
        "sltiu": validate_2_itype,
        "xori": validate_2_itype,
        "li": validate_1_itype,
        "bgez": validate_1_itype,
        "bgtz": validate_1_itype,
        "blez": validate_1_itype,
        "bltz": validate_1_itype,
        "lui": validate_1_itype,
        "sw": validate_optional_2_itype,
        "lw": validate_optional_2_itype,
        "lb": validate_optional_2_itype,
        "lbu": validate_optional_2_itype,
        "lh": validate_optional_2_itype,
        "lhu": validate_optional_2_itype,
        "lwc1": validate_optional_2_itype,
        "sb": validate_optional_2_itype,
        "sh": validate_optional_2_itype,
        "swc1": validate_optional_2_itype,
    }
    try:
        func = switch[instruction.command]
        res = func(instruction)
    except:
        res = False
    return res


def validate_3_rtype(instruction) -> bool:
    """Validates R-Type instructions with 3 registers 
    
    Parameters
    ----------
    instruction : [R-Type]
        [description]
    
    Returns
    -------
    bool
        [Syntax correct or not]
    """
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


def validate_0_rtype(instruction) -> bool:
    rd = instruction.destination_register
    rs = instruction.source_register
    rt = instruction.target_register

    check1 = rd is None
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

    return check1 and check2 and check3 and check4


def validate_optional_2_itype(instruction) -> bool:
    destination = instruction.destination_register
    target = instruction.target_register
    immediate = instruction.immediate

    check1 = destination is not None
    check3 = immediate is not None
    check4 = target is None

    return check1 and check3 and check4


def validate_1_itype(instruction) -> bool:
    destination = instruction.destination_register
    target = instruction.target_register
    immediate = instruction.immediate
    source = instruction.source_register

    check1 = destination is not None
    check2 = target is None
    check3 = immediate is not None
    check4 = source is None

    return check1 and check2 and check3 and check4

