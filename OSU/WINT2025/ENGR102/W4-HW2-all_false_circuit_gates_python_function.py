# ENGR102 W4 HW2 Assignment: Return true when exactly 3 inputs are False (and False otherwise)

def gate_and(a, b):
    """ 2-input AND gate (a ^ b) """
    gate1 = a and b
    return bool(gate1)

def gate_not(a):
    """ 1-input NOT gate ( ~a ) """
    gate2 = not a
    return bool(gate2)

def all_false(a, b, c):
    """ Two 2-input gates (~a ^ ~b ^ ~c) """
    # Inversing the inputs with NOT gates here before running them through the 2-input gates
    gate3 = gate_not(a) # ~a
    gate4 = gate_not(b) # ~b
    gate5 = gate_not(c) # ~c
    
    # Using AND to combine the first two inverted inputs here before combining with the third inverted input
    gate6 = gate_and(gate3, gate4) # (~a ^ ~b)
    
    # Using AND gate to combine the result of the first AND gate with the third inverted input to get the final output
    gate7 = gate_and(gate5, gate6) # (~a ^ ~b ^ ~c)
    
    return gate7 # Returning the final output

print(all_false(0, 0, 0)) # Expected output: True
print(all_false(0, 0, 1)) # Expected output: False
print(all_false(0, 1, 0)) # Expected output: False
print(all_false(0, 1, 1)) # Expected output: False
print(all_false(1, 0, 0)) # Expected output: False
print(all_false(1, 0, 1)) # Expected output: False
print(all_false(1, 1, 0)) # Expected output: False
print(all_false(1, 1, 1)) # Expected output: False

# Sneaky

# Nabbed some fancy truth table formatting ideas from people better at coding than me
print(" a\tb\tc\t | \tall_false")
print("--\t--\t--\t | \t--------")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            # This is the output of my function - praying it works
            Q_output = all_false(a, b, c)
            print(f"{a}\t{b}\t{c}\t | \t{Q_output}")