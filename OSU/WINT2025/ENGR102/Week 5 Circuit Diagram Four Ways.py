def gate_and(input1, input2):
    """ an AND gate (input1 ^ input2) """
    gate1 = input1 and input2
    return bool(gate1)
                

def gate_or(input1, input2):
    """ an OR gate (input1 v input2) """
    gate1 = input1 or input2
    return bool(gate1)
                           

def gate_xor(input1, input2):
    """ an XOR gate ((input1 ^ ~input2) v (~input1 ^ input2)) """
    gate1 = input1 and not input2
    gate2 = input2 and not input1
    return bool(gate1 or gate2)                     


def gate_nand(input1, input2):
    """ a NAND gate (~(input1 ^ input2)) """
    gate1 = not(input1 and input2)
    return bool(gate1)
                                    

def gate_nor(input1, input2):
    """ a NOR gate (~(input1 v input2)) """
    gate1 = not(input1 or input2)
    return bool(gate1)
                                    

def gate_not(input1):
    """ a NOT gate (~input1) """
    return bool(not input1)

def one_false(A, B, C, D):
    # Doing the XOR
    xor_ab = gate_xor(A, B)
    xor_cd = gate_xor(C, D)
    
    # Doing the two AND parts for A, B (top) side and C, D (bottom) side
    # top side: The (C AND D) then an AND with the (A XOR B)
    and_cd = gate_and(C, D)
    top_side = gate_and(and_cd, xor_ab)
    
    # bottom side: The (A AND B) then an AND with the (C XOR D)
    and_ab = gate_and(A, B)
    bottom_side = gate_and(and_ab, xor_cd)
    
    # Combining top and bottom sides with an OR gate
    Q = gate_or(top_side, bottom_side)
    return Q

print(one_false(1, 1, 1, 1))