
from Mod1.stack import (create_array_stack, array_stack_push, array_stack_pop, create_linked_stack, linked_stack_push,
                        linked_stack_pop, linked_stack_find_index, linked_stack_push_v2)


def copies_for_appends(n, next_capacity, start_capacity = 5):
    capacity = start_capacity
    copies = 0
    for size in range(n):
        if size == capacity:
            copies += size
            capacity = next_capacity(capacity)
    return copies


strategies = [('add 1', lambda c: c+1),
              ('add 10', lambda c: c + 10),
              ('double', lambda c: c*2),
              ('tripe', lambda c: c*3)]

for n in 100, 1000, 10000, 1000000:
    print('n = ', n)
    for name, grow in strategies:
        copies = copies_for_appends(n, grow)
        print('   %-10s %12s copies %8.2f per append' % (name, format(copies, ','), copies / n))





def make_big_stacks():
    array_stack = create_array_stack(5)
    linked_stack = create_linked_stack()

    for i in range(20):
        print(f'Pushing {i} to the stacks')
        array_stack_push(array_stack, i)
        linked_stack_push(linked_stack, i)
    pass


# make_big_stacks()