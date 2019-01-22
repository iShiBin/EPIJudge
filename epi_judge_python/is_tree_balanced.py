from test_framework import generic_test

import collections

def is_balanced_binary_tree(tree):
    return get_depth(tree) != -1

def get_depth(node):
    if node is None: return 0
    left = get_depth(node.left)
    right = get_depth(node.right)

    if left == -1 or right == -1 or abs(left-right) > 1:
        return -1   # quick return if unbalanced
    
    return 1 + max(left, right)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
