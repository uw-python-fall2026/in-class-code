from collections import deque

## Python-list backed queue
def create_queue_list():
    return {
        'data': []
    }

def queue_list_enqueue(queue, item):
    queue['data'].append(item)

def queue_list_dequeue(queue):
    return queue['data'].pop(0)


def create_queue_deque():
    return deque()

def deque_enqueue(deque, item):
    deque.append(item)

def deque_dequeue(deque):
    return deque.popleft()




