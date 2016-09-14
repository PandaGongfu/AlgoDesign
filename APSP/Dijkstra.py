import heapq

class graph:

    def __init__(self, params):
        self.graph = params[0]
        self.vertices = params[1]

        self.processed = set()
        self.unprocessed = params[1]
        self.shortest = {}
        for vertex in self.vertices:
            self.shortest.setdefault(vertex, 0)


def Dijkstra_sp(path_graph, s, in_edges):
    path_graph.processed.add(s)
    path_graph.unprocessed.remove(s)

    greedy_dist = []
    ww = s

    while len(path_graph.unprocessed):
        for w in path_graph.unprocessed:
            for v in in_edges[w]:
                if v == ww:
                    heapq.heappush(greedy_dist, (path_graph.shortest[v] + path_graph.graph[(v, w)], w))

        min_d, ww = heapq.heappop(greedy_dist)
        path_graph.processed.add(ww)
        path_graph.unprocessed.remove(ww)
        path_graph.shortest[ww] = min_d

        # remove nodes that've been processed from heap
        greedy_dist = [x for x in greedy_dist if x[1] != ww]

    return path_graph.shortest



