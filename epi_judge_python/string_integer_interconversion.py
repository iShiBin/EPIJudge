from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):        
    is_negative = False

    if x < 0:
        is_negative = True
        x = -x

    string = []
    while True:
        string.append(chr(x % 10 + ord('0')))
        x = x // 10
        if x == 0: break
    
    return ('-' if is_negative else '') + ''.join(reversed(string))


def string_to_int(s):
    is_negative = True if s[0] == '-' else False
    if is_negative: s = s[1:]
    integer = 0
    for c in s:
        integer *= 10
        integer += ord(c) - ord('0')
    
    if is_negative: return -1 * integer
    else: return integer


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
