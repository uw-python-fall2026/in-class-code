import random, time
from bst_mon import bst_insert_iterative, bst_search_iterative

rng = random.Random(3)
values = rng.sample(range(50000), 10000)

shuffled = None
for v in values:
    shuffled = bst_insert_iterative(shuffled, v)

chain = None
for v in sorted(values):
    chain = bst_insert_iterative(chain, v)

for name, tree in (('random order', shuffled), ('sorted_order', chain)):
    start = time.perf_counter()
    for v in values:
        bst_search_iterative(tree, v)
    print(name, round(time.perf_counter() - start, 4), 'seconds for 5000 searches')