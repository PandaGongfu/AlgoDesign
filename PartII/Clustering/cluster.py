import heapq
import re

class graph:

    def __init__(self, params):
        self.graph = params[0]
        self.vertices = params[1]

        self.leaders = {}
        for vertex in self.vertices:
            self.leaders[vertex] = vertex


    def read_graph(file_handle):
        lines = file_handle.read().split('\n')
        p = re.compile('-?\d+')

        graph = {}
        vertices = []
        nvertices = list(map(int, p.findall(lines[0])))[0]

        for l in lines[1:-1]:
            u, v, cost = map(int, p.findall(l))
            vertices.extend([u, v])
            graph[tuple([u, v])] = cost

        all_vertices = sorted(list(set(vertices)))
        assert(len(all_vertices) == nvertices)
        return [graph, all_vertices]


def Union_Find(graph, K):
    ncluster = len(graph.vertices)
    while ncluster > K:
        greedy_dist = {}
        for v, w in graph.graph.keys():
            if graph.leaders[w] != graph.leaders[v]:
                greedy_dist[(v, w)] = graph.graph[(v, w)]

        (vv, ww) = heapq.nsmallest(1, greedy_dist, key=greedy_dist.get)[0]
        leader_v = graph.leaders[vv]
        leader_w = graph.leaders[ww]

        nv = sum([x == leader_v for _, x in graph.leaders.items()])
        nw = sum([x == leader_w for _, x in graph.leaders.items()])

        leader_smaller = leader_v
        leader_larger = leader_w
        if nv > nw:
            leader_smaller = leader_w
            leader_larger = leader_v

        for vertex, leader in graph.leaders.items():
            if leader == leader_smaller:
                graph.leaders[vertex] = leader_larger
        ncluster -= 1
        print(ncluster)


fh = open('clustering1.txt', 'r')
cluster_graph = graph(graph.read_graph(fh))
fh.close()

K = 4
Union_Find(cluster_graph, K)

max_spacing = 1e6
for v, w in cluster_graph.graph.keys():
    if cluster_graph.leaders[v] != cluster_graph.leaders[w]:
        if cluster_graph.graph[(v, w)] < max_spacing:
            max_spacing = cluster_graph.graph[(v, w)]

