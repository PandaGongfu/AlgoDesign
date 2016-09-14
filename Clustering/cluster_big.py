import re


class graph:
    def __init__(self, params):
        self.vertices = params

        self.parents = {}
        self.ranks = {}
        for vertex in self.vertices:
            self.parents[vertex] = vertex
            self.ranks[vertex] = 0


def read_graph(file_handle):
    lines = file_handle.read().split('\n')
    p = re.compile('\d+')

    vertices = set()
    nvertices, _ = map(int, p.findall(lines[0]))
    for _, l in enumerate(lines[1:-1]):
        vertices.add(''.join([x.strip() for x in p.findall(l)]))
    return vertices


def not_str(bit):
    return '1' if bit == '0' else '0'


def find_root(graph, v):
    if graph.parents[v] != v:
        graph.parents[v] = find_root(graph, graph.parents[v])
    return graph.parents[v]


def union_rank(graph, vv, ww):
    pv = find_root(graph, vv)
    pw = find_root(graph, ww)

    if graph.ranks[pv] > graph.ranks[pw]:
        graph.parents[pw] = pv
    else:
        graph.parents[pv] = pw
        if graph.ranks[pv] == graph.ranks[pw]:
            graph.ranks[pw] += 1


def find_k(graph):
    ncluster = len(graph.vertices)

    for node in list(graph.vertices):
        p_nodes = set()
        # find all dist 1 nodes:
        for i in range(len(node)):
            p_nodes.add(node[:i]+not_str(node[i])+node[i+1:])

        # find all dist 2 nodes:
        for m in range(len(node)):
            for n in range(m+1, len(node)):
                p_nodes.add(node[:m]+not_str(node[m])+node[m+1:n]+not_str(node[n])+node[n+1:])

        nodes_12 = p_nodes.intersection(graph.vertices)
        for node12 in nodes_12:
            if find_root(graph, node) != find_root(graph, node12):
                union_rank(graph, node, node12)
                ncluster -= 1

    return ncluster


fh = open('clustering_big.txt', 'r')
cluster_graph = graph(read_graph(fh))
fh.close()

ncluster = find_k(cluster_graph)
print(ncluster)
