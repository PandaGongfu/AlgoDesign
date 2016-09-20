from itertools import combinations
import math
from collections import defaultdict
from copy import deepcopy

def read_input(file_name):
    fh = open(file_name, 'r')
    lines = fh.read().split('\n')

    ncities = int(lines[0])
    coordinates = {}
    distances = {}
    for i, l in enumerate(lines[1:-1]):
        coordinates[i] = tuple(map(float, l.split()))
    assert(ncities == len(coordinates))

    for a, b in combinations(range(ncities), 2):
        distances[(a, b)] = dist(coordinates[a], coordinates[b])
        distances[(b, a)] = distances[(a, b)]

    fh.close()
    return ncities, distances


def p_subsets(n, ncities):
    s = range(1, ncities)
    p_subsets = []
    p_subsets.extend([tuple(k) for k in combinations(s, n)])
    return p_subsets


def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def bit_str(s):
    nbit = list('0' * 25)
    for k in s:
        nbit[k] = '1'
    return ''.join(nbit)


ncities, distances = read_input('tsp.txt')
A = defaultdict(list)

for k in range(1, ncities):
    A[bit_str((k,))] = [0] * ncities
    A[(bit_str((k,)))][k] = distances[(k, 0)]

for m in range(2, ncities):
    S = p_subsets(m, ncities)
    A_last = deepcopy(A)
    del A
    A = defaultdict(list)

    print('m= ', m)
    print('len= ', len(S))
    count = 0
    for s in S:
        count += 1
        if not count % 10000:
            print(count)
        A[bit_str(s)] = [0] * ncities
        for j in s:
            A[bit_str(s)][j] = min([A_last[bit_str(tuple(set(s) - set([j])))][k] + distances[(k, j)]
                                    for k in s if k != j])
    del A_last
    A_last = defaultdict(list)

tsp_dist = min([A[bit_str(range(1, ncities))][j] + distances[(j, 0)] for j in range(1, ncities)])
print(tsp_dist)