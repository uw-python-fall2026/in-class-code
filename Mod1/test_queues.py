from unittest import TestCase
from Mod1.queues import * ##create_queue_list, queue_list_enqueue, queue_list_dequeue


class Test(TestCase):
    def test_items_dequeue_in_order(self):
        ## Set up test
        queue = create_queue_list()
        queue_list_enqueue(queue, 'Squirtle')
        queue_list_enqueue(queue, 'Evee')
        queue_list_enqueue(queue, 'Pikachu')

        self.assertEqual('Squirtle', queue_list_dequeue(queue))
        self.assertEqual('Evee', queue_list_dequeue(queue))
        self.assertEqual('Pikachu', queue_list_dequeue(queue))



    def test_items_dequeue_in_order_from_deque(self):
        ## Set up test
        queue = create_queue_deque()
        deque_enqueue(queue, 'Squirtle')
        deque_enqueue(queue, 'Evee')
        deque_enqueue(queue, 'Pikachu')

        self.assertEqual('Squirtle', deque_dequeue(queue))
        self.assertEqual('Evee', deque_dequeue(queue))
        self.assertEqual('Pikachu', deque_dequeue(queue))