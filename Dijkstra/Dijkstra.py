import heapq

class graph:

    def __init__(self, params):
        self.graph = params[0]
        self.vertices = params[1]

        self.processed = []
        self.shortest = {}
        for vertex in self.vertices:
            self.shortest.setdefault(vertex, 0)


    def read_graph(handle):
        lines = fh.read().split('\n')
        graph = {}
        vertices = []
        for l in lines[:-1]:
            vdata = l.split('\t')[:-1]
            vertex = int(vdata[0])
            vertices.append(vertex)
            edata = [tuple(map(lambda x: int(x), x.split(','))) for x in vdata[1:]]

            for edge in edata:
                graph.setdefault((vertex, edge[0]), 0)
                graph[(vertex, edge[0])] = edge[1]

        return [graph, sorted(vertices)]


fh = open('DijkstraData.txt', 'r')
path_graph = graph(graph.read_graph(fh))
fh.close()

path_graph.processed = [path_graph.vertices.pop(0)]
unprocessed = list(set(path_graph.vertices) - set(path_graph.processed))

while len(unprocessed):
    greedy_dist = {}

    for v in path_graph.processed:
        for w in unprocessed:
            greedy_dist[(v, w)] = path_graph.shortest[v] + path_graph.graph.get((v, w), 1e6)

    (vv, ww) = heapq.nsmallest(1, greedy_dist, key=greedy_dist.get)[0]
    path_graph.processed.append(ww)
    path_graph.shortest[ww] = greedy_dist[(vv, ww)]
    unprocessed = list(set(path_graph.vertices) - set(path_graph.processed))

dests =[7,37,59,82,99,115,133,165,188,197]
arr=[]
for dest in dests:
    arr.append(path_graph.shortest[dest])


