import heapq
import re

class graph:

    def __init__(self, params):
        self.graph = params[0]
        self.vertices = params[1]

        self.processed = []
        self.MST = {}


    def read_graph(file_handle):
        lines = file_handle.read().split('\n')
        p = re.compile('-?\d+')

        graph = {}
        vertices = []
        nvertices, _ = map(int, p.findall(lines[0]))

        for l in lines[1:-1]:
            u, v, cost = map(int, p.findall(l))
            vertices.extend([u, v])
            graph[tuple([u, v])] = cost
            graph[tuple([v, u])] = cost

        all_vertices = sorted(list(set(vertices)))
        assert(len(all_vertices) == nvertices)
        return [graph, all_vertices]


fh = open('edges.txt', 'r')
MST_graph = graph(graph.read_graph(fh))
fh.close()

MST_graph.processed = [MST_graph.vertices.pop(0)]
unprocessed = list(set(MST_graph.vertices) - set(MST_graph.processed))

while len(unprocessed):
    greedy_dist = {}

    for v in MST_graph.processed:
        for w in unprocessed:
            greedy_dist[(v, w)] = MST_graph.graph.get((v, w), 1e6)

    (vv, ww) = heapq.nsmallest(1, greedy_dist, key=greedy_dist.get)[0]
    print('%d %d %d' % (vv, ww, greedy_dist[(vv, ww)]))
    MST_graph.processed.append(ww)
    MST_graph.MST[(vv, ww)] = greedy_dist[(vv, ww)]
    unprocessed = list(set(MST_graph.vertices) - set(MST_graph.processed))

sum(MST_graph.MST.values())