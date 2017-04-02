import collections, io
from itertools import chain

stats = collections.defaultdict(lambda: 0)

with open('d:\data.txt', 'r') as fp:
    for char in chain.from_iterable(fp):
        stats[char] += 1
##for char in stats:
##    print(char)
print('\n'.join(stats))


