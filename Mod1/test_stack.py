from unittest import TestCase
from Mod1.stack import (create_array_stack, array_stack_push, array_stack_pop, create_linked_stack, linked_stack_push,
                        linked_stack_pop, linked_stack_find_index, linked_stack_push_v2)

class Test(TestCase):
    def test_push_then_pop_returns_values_newest_first(self):
        ## Set up the test
        stack = create_array_stack(3)
        array_stack_push(stack, 'a')
        array_stack_push(stack, 'b')

        ## Test/Assert
        self.assertEqual('b', array_stack_pop(stack))
        self.assertEqual('a', array_stack_pop(stack))
        self.assertEqual(0, stack['size'])

    def test_pop_on_an_empty_stack_throws(self):
        stack = create_array_stack(3)
        with self.assertRaises(IndexError):
            array_stack_pop(stack)

    def test_push_on_stack_full_throws(self):
        ## Test set-up
        stack = create_array_stack(3)
        array_stack_push(stack, 'a')
        array_stack_push(stack, 'b')
        array_stack_push(stack, 'c')

        with self.assertRaises(IndexError):
            array_stack_push(stack, 'd')

    def test_linked_push_then_pop_returns_values_newest_first(self):
        ## Set up the test
        stack = create_linked_stack()
        linked_stack_push(stack, 'a')
        linked_stack_push(stack, 'b')

        ## Test/Assert
        self.assertEqual('b', linked_stack_pop(stack))
        self.assertEqual('a', linked_stack_pop(stack))
        self.assertEqual(0, stack['size'])

    def test_linked_push_v2_then_pop_returns_values_newest_first(self):
        ## Set up the test
        stack = create_linked_stack()
        linked_stack_push_v2(stack, 'a')
        linked_stack_push_v2(stack, 'b')

        ## Test/Assert
        self.assertEqual('b', linked_stack_pop(stack))
        self.assertEqual('a', linked_stack_pop(stack))
        self.assertEqual(0, stack['size'])


    def test_linked_pop_on_an_empty_stack_throws(self):
        stack = create_linked_stack()
        with self.assertRaises(IndexError):
            linked_stack_pop(stack)

    def test_linked_push_on_stack_full_throws(self):
        ## Test set-up
        stack = create_linked_stack()
        linked_stack_push(stack, 'a')
        linked_stack_push(stack, 'b')
        linked_stack_push(stack, 'c')

        with self.assertRaises(IndexError):
            linked_stack_push(stack, 'd')

    def test_linked_find_nonexistent_value(self):
        ## Test set-up
        stack = create_linked_stack()
        linked_stack_push(stack, 'a')
        linked_stack_push(stack, 'b')
        linked_stack_push(stack, 'c')

        self.assertEqual(-1, linked_stack_find_index(stack, 'd'))

    def test_linked_find_middle(self):
        stack = create_linked_stack()
        linked_stack_push(stack, 'a')
        linked_stack_push(stack, 'b')
        linked_stack_push(stack, 'c')

        self.assertEqual(1, linked_stack_find_index(stack, 'b'))

