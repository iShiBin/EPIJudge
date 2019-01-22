from test_framework import generic_test

def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    if not tree: return []

    result = []
    level_nodes = [tree]

    while level_nodes:
        result.append([node.data for node in level_nodes])
        level_nodes = [child for nodes in level_nodes for child in (nodes.left, nodes.right) if child]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
