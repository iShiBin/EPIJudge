from test_framework import generic_test

def count_bits(x):
    # n = 0
    # while x:
    #     n += x & 1
    #     x >>= 1
    # return n
    return bin(x).count('1')

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
