import numpy as np
from copy import deepcopy

fh = open('kargerMinCut.txt', 'r')
lines = fh.read().split('\n')

input_arr = []
for l in lines[:-1]:
    input_arr.append([int(x) - 1 for x in l.split('\t')[:-1]])
fh.close()

mincut = 100
for k in range(0, 100):
    arr = deepcopy(input_arr)
    n = len(arr)
    v = -1
    choice_range = range(0, len(arr))

    while n > 2:
        choice_range = list(set(choice_range) - set([v])) # remove v from vertices
        u = np.random.choice(choice_range, 1)[0]  # need to revise so that edge is uniformly chosen not vertices
        v = np.random.choice(arr[u][1:], 1)[0]

        # merge u, v into u
        arr[u].extend(arr[v][1:]) # move v-edge to u-edge

        for row in arr[v][1:]:
            arr[row] = [u if x == v else x for x in arr[row]] # make edge-v to edge-u

        arr[u] = [u] + [x for x in arr[u] if x != u] # remove self-loop
        arr[v] = [0] * len(arr[v])

        n -= 1

    if mincut > len(arr[u])-1:
        mincut = len(arr[u])-1

print(mincut)
