import Dijkstra
from copy import deepcopy


def read_input(file_name):
    fh = open(file_name, 'r')
    lines = fh.read().split('\n')

    nvertices, nedges = map(int, lines[0].split())
    vertices = set()
    ecost = {}
    in_edges = {}
    for l in lines[1:-1]:
        u, v, cost = map(int, l.split())
        ecost[(u, v)] = cost
        vertices |= set([u, v])
        in_edges.setdefault(v, []).append(u)

    assert(nvertices == len(vertices))
    assert(nedges == len(ecost))

    fh.close()
    return ecost, vertices, in_edges


def bellman_ford(ecost, vs, in_edges, s):
    A = {}
    A_last = {}
    cycle = False
    for v in vs:
        A[v] = 1e6 if s == v else 0

    for _ in range(1, len(vs)+1):
        A_last = deepcopy(A)
        for v in vs:
            A[v] = min(A_last[v], min([A_last[w] + ecost[(w, v)] for w in in_edges[v]]))

        if A_last == A:  # early stop
            return cycle, A_last

    if A_last != A:
        cycle = True
    return cycle, A_last


def johnson(file_name):
    ecost, vertices, in_edges = read_input(file_name)
    s = 999999
    for v in vertices:
        ecost[(s, v)] = 0

    cycle, bf_sp = bellman_ford(ecost, vertices, in_edges, s)
    if cycle:
        return 'NULL'

    new_ecost = {}
    for (u, v) in ecost.keys():
        if s != u:
            new_ecost[(u, v)] = ecost[(u, v)] + bf_sp[u] - bf_sp[v]

    min_sp = []
    for s_node in vertices:
        path_graph = Dijkstra.graph((new_ecost, deepcopy(vertices)))
        djk_sp = Dijkstra.Dijkstra_sp(path_graph, s_node, in_edges)
        for v in vertices:
            djk_sp[v] -= bf_sp[s_node] - bf_sp[v]
        min_sp.append(min(list(djk_sp.values())))

    return min(min_sp)


file_names = ['g1.txt', 'g2.txt', 'g3.txt']
min_apsp = []
for file_name in file_names:
    res = johnson(file_name)
    if 'NULL' != res:
        min_apsp.append(res)
if len(min_apsp):
    print(min(min_apsp))
else:
    print('NULL')







