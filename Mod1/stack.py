

def create_array_stack(capacity):
    return {'data': [None] * capacity, 'size': 0}


def array_stack_pop(stack):
    if stack['size'] == 0:
        raise IndexError('Cannot pop from an empty stack')
    elem = stack['data'][stack['size'] - 1]
    stack['size'] -= 1
    return elem




def array_resize_add1(stack):
    new_data_array = [None] * (len(stack['data']) + 1)
    for ind, item in enumerate(stack['data']):
        new_data_array[ind] = item

    stack['data'] = new_data_array


def array_resize_add10(stack):
    new_data_array = [None] * (len(stack['data']) + 10)
    for ind, item in enumerate(stack['data']):
        new_data_array[ind] = item

    stack['data'] = new_data_array

def array_resize_double(stack):
    new_data_array = [None] * (len(stack['data']) * 2)
    for ind, item in enumerate(stack['data']):
        new_data_array[ind] = item

    stack['data'] = new_data_array


def array_stack_grow(stack):
    new_data = [None] * (len(stack['data']) * 2)
    for i in range(stack['size']):
        new_data[i] = stack['data'][i]
    stack['data'] = new_data


def array_stack_push_growing(stack, value):
    if stack['size'] == len(stack['data']):
        array_stack_grow(stack)
    stack['data'][stack['size']] = value
    stack['size'] += 1


def array_stack_push(stack, elem):
    if stack['size'] == len(stack['data']):
        # raise IndexError('Stack is full')
        array_resize_double(stack)
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


def linked_stack_find_index(stack, value):
    cur_node = stack['head']
    index = 0
    while cur_node is not None:
        ## Check payload
        if cur_node['payload'] == value:
            return index
        ## Return index OR get next one
        cur_node = cur_node['next']
        index += 1
    return -1
    pass

def linked_stack_push_v2(stack, value):
    node = create_node(value)

    node['next'] = stack['head']
    stack['head'] = node

    stack['size'] += 1







