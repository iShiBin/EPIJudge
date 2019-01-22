from test_framework import generic_test

# 4.1 Computing the parity of a word
# How would you compute the parity of a very large number of 64-bit words?

def parity(x):
    """
    x: binary word like 0b...
    return parity of the input x
    """
    return xor_half(x)

def xor_half(x, length=64):
    x ^= x >> (length//2)
    if length == 2:
        return x & 0x1
    else:
        return xor_half(x, length//2)

if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
