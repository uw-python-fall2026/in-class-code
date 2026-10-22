from collections import deque


def create_tree_node(value, left=None, right=None):
    return {
        'payload': value,
        'left': left,
        'right': right
    }


def preorder_dfs(node, out=[]):
    if node is None:
        return
    out.append(node['payload'])
    preorder_dfs(node['left'], out)
    preorder_dfs(node['right'], out)


def inorder_dfs(node, out=[]):
    if node is None:
        return
    inorder_dfs(node['left'], out)
    out.append(node['payload'])
    inorder_dfs(node['right'], out)


def postorder_dfs(node, out=[]):
    if node is None:
        return
    postorder_dfs(node['left'], out)
    postorder_dfs(node['right'], out)
    out.append(node['payload'])


root = create_tree_node(8,
                        create_tree_node(3,
                                         create_tree_node(1), ## Left of 3
                                         create_tree_node(6, create_tree_node(4), create_tree_node(7))),
                        create_tree_node(10, None, create_tree_node(14, create_tree_node(13), None)))

order = []
preorder_dfs(root, order)
print(order)

inorder = []
inorder_dfs(root, inorder)
print(inorder)



postorder = []
postorder_dfs(root, postorder)
print(postorder)




def bfs(root):
    out = []
    nodes_to_visit = deque()
    if root is not None:
        nodes_to_visit.append(root)
    while nodes_to_visit:
        node = nodes_to_visit.popleft()
        out.append(node['payload'])
        if node['left'] is not None:
            nodes_to_visit.append(node['left'])
        if node['right'] is not None:
            nodes_to_visit.append(node['right'])

    return out

## 8 3 10 1 6 14 4 7 13

print(bfs(root))


def mystery_traversal_dfs(root):
    out = []
    nodes_to_visit = []
    if root is not None:
        nodes_to_visit.append(root)
    while nodes_to_visit:
        node = nodes_to_visit.pop()
        out.append(node['payload'])
        if node['left'] is not None:
            nodes_to_visit.append(node['left'])
        if node['right'] is not None:
            nodes_to_visit.append(node['right'])

    return out


print(mystery_traversal_dfs(root))





