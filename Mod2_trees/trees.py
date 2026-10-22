


def create_tree_node(value, left=None, right=None):
    return {
        'payload': value,
        'left': left,
        'right': right
    }

def tree_size(node):
    if node is None:
        print("Node is None, returning 0")
        return 0
    print(f"Adding Node {node['payload']} to the size calculation")
    return (1 +
            tree_size(node['left']) +
            tree_size(node['right']))

def tree_height(node):
    if node is None:
        return -1
    return (1 +
            max(tree_height(node['left']),
                tree_height(node['right'])))


root = create_tree_node(8,
                        create_tree_node(3,
                                         create_tree_node(1), ## Left of 3
                                         create_tree_node(6, create_tree_node(4), create_tree_node(7))),
                        create_tree_node(10, None, create_tree_node(14, create_tree_node(13), None)))


print(root['left']['right']['payload'])


print(tree_size(root))

print("Finding tree height")
print(tree_height(root))

print('\n\n\n\n')
#
one_node = create_tree_node(42)
print(tree_size(one_node))
print(tree_height(one_node))

# print(root['right']['left'])



