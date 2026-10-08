

def create_array_stack(capacity):
    return {'data': [None] * capacity, 'size': 0}


def array_stack_pop(stack):
    if stack['size'] == 0:
        raise IndexError('Cannot pop from an empty stack')
    elem = stack['data'][stack['size'] - 1]
    stack['size'] -= 1
    return elem


def array_stack_push(stack, elem):
    if stack['size'] == len(stack['data']):
        raise IndexError('Stack is full')
    next_index = stack['size']

    stack['data'][next_index] = elem
    stack['size'] += 1
    pass


def create_node(value):
    return {'payload': value, 'next': None}


def create_linked_stack():
    return {'head': None, 'size': 0}


def linked_stack_push(stack, elem):
    new_node = create_node(elem)
    new_node['next'] = stack['head']
    stack['head'] = new_node
    stack['size'] += 1
    pass


def linked_stack_pop(stack):
    if stack['size'] == 0:
        raise IndexError('Cannot pop from an empty stack')
    data_node = stack['head']

    stack['head'] = data_node['next']
    stack['size'] -= 1
    return data_node['payload']
