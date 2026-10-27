


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

def bst_search_iterative(root, value):
    cur_node = root

    while cur_node is not None:
        # print(f'cur_node is {cur_node['payload']}')
        if cur_node['payload'] == value:
            return cur_node
        if value < cur_node['payload']:
            # print("Going to the left")
            cur_node = cur_node['left']
        else:
            # print("Going to the right")
            cur_node = cur_node['right']

    return None

def bst_insert_iterative(root, value):
    if root is None:
        return create_tree_node(value)
    node = root
    while True:
        if value == node['payload']:
            return root
        side = 'left' if value < node['payload'] else 'right'
        if node[side] is None:
            node[side] = create_tree_node(value)
            return root
        node = node[side]


root = create_tree_node(8,
                        create_tree_node(3,
                                         create_tree_node(1), ## Left of 3
                                         create_tree_node(6, create_tree_node(4), create_tree_node(7))),
                        create_tree_node(10, None, create_tree_node(14, create_tree_node(13), None)))


print(bst_search_iterative(root, 9))