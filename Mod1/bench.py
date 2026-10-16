import sys, time, tracemalloc
from collections import deque
from queue import Queue, SimpleQueue
from stack import *


def best(fn, repeat=5):
    times = []
    for _ in range(repeat):
        t = time.perf_counter(); fn(); times.append(time.perf_counter() - t)
    return min(times)


print('Python', sys.version.split()[0], sys.platform)

print('\n== 1. push n then pop n (seconds, best of 3) ==')
print('%9s %12s %14s %12s %12s' % ('n', 'array fixed', 'array growing', 'linked', 'list'))
for n in (10_000, 100_000, 1_000_000):
    def a():
        s = create_array_stack(n)
        for i in range(n): array_stack_push(s, i)
        for _ in range(n): array_stack_pop(s)
    def g():
        s = create_array_stack(4)
        for i in range(n): array_stack_push_growing(s, i)
        for _ in range(n): array_stack_pop(s)
    def l():
        s = create_linked_stack()
        for i in range(n): linked_stack_push(s, i)
        for _ in range(n): linked_stack_pop(s)
    def p():
        s = []
        for i in range(n): s.append(i)
        for _ in range(n): s.pop()
    print('%9s %12.4f %14.4f %12.4f %12.4f' % (format(n, ','), best(a, 3), best(g, 3), best(l, 3), best(p, 3)))

print('\n== 2. memory for n = 100,000 values (tracemalloc, MB) ==')
n = 100_000
vals = list(range(n))   # created outside, so only the container is measured


def mem(builder):
    tracemalloc.start(); before = tracemalloc.get_traced_memory()[0]
    obj = builder()
    after = tracemalloc.get_traced_memory()[0]; tracemalloc.stop()
    return (after - before) / 1e6, obj


def build_array():
    s = create_array_stack(n)
    for v in vals: array_stack_push(s, v)
    return s


def build_growing():
    s = create_array_stack(4)
    for v in vals: array_stack_push_growing(s, v)
    return s


def build_linked():
    s = create_linked_stack()
    for v in vals: linked_stack_push(s, v)
    return s


for name, b in (('array, exact capacity', build_array), ('array, growing', build_growing),
                ('linked stack (dict nodes)', build_linked), ('python list', lambda: list(vals)),
                ('deque', lambda: deque(vals))):
    m, obj = mem(b); print('%-28s %7.2f MB   %6.1f bytes/value' % (name, m, m * 1e6 / n))

print('\n== 3. queue: fill with n values, then remove all from the front (seconds, best of 3) ==')
print('%9s %14s %14s %14s %14s' % ('n', 'list.pop(0)', 'deque.popleft', 'queue.Queue', 'SimpleQueue'))
for n in (10_000, 20_000, 40_000, 80_000, 160_000):
    def lp():
        q = list(range(n))
        while q: q.pop(0)
    def dq():
        q = deque(range(n))
        while q: q.popleft()
    def qq():
        q = Queue()
        for i in range(n): q.put(i)
        while not q.empty(): q.get()
    def sq():
        q = SimpleQueue()
        for i in range(n): q.put(i)
        while not q.empty(): q.get()
    print('%9s %14.4f %14.4f %14.4f %14.4f' % (format(n, ','), best(lp, 3), best(dq, 3), best(qq, 3), best(sq, 3)))

print('\n== 4. single operations on 1,000,000 values (microseconds per operation) ==')
n = 1_000_000
L = list(range(n)); D = deque(range(n))


def per_op(fn, reps):
    return best(lambda: [fn() for _ in range(reps)], 5) / reps * 1e6


print('list[n//2]               %9.3f' % per_op(lambda: L[n // 2], 20000))
print('deque[n//2]              %9.3f' % per_op(lambda: D[n // 2], 2000))
print('list insert(0)+pop(0)    %9.3f' % per_op(lambda: (L.insert(0, 1), L.pop(0)), 200))
print('deque appendleft+popleft %9.3f' % per_op(lambda: (D.appendleft(1), D.popleft()), 20000))