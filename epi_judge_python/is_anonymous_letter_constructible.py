from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    counter = Counter(letter_text)
    for c in magazine_text:
        if c in counter:
            counter[c] -= 1
            if counter[c] == 0: del counter[c]
    if counter: return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
