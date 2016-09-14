def read_input(file_name):
    fh = open(file_name, 'r')
    lines = fh.read().split('\n')

    sacksize, _ = map(int, lines[0].split())
    values = []
    weights = []
    for l in lines[1:-1]:
        value, weight = map(int, l.split())
        values.append(value)
        weights.append(weight)

    fh.close()
    return values, weights, sacksize


values, weights, sacksize = read_input('knapsack1.txt')
caps = range(sacksize+1)
VS = {}
for x in caps:
    VS[(-1, x)] = 0

for i, v in enumerate(values):
    for x in caps:
        if x > weights[i]:
            VS[(i, x)] = max(VS[(i-1, x)], v + VS[(i-1, x-weights[i])])
        else:
            VS[(i, x)] = VS[(i-1, x)]

print(VS[(len(values)-1, sacksize)])

"""retrace optimal solution"""
# S = []
# x = caps[-1]
# for i in np.arange(nitems-1, -1, -1):
#     v = values[i]
#     if x > weights[i] and VS[(i, x)] <= v + VS[(i-1, x-weights[i])]:
#         S.append(v)
#         x -= weights[i]


