from collections import Counter

class dgraph:

    def __init__(self, params):
        self.graph = params[0]
        self.vertices = params[1]
        self.explored = {}
        self.ftime = {}
        self.leaders = {}
        for vertex in self.vertices:
            self.explored.setdefault(vertex, False)
            self.ftime.setdefault(vertex, 0)
            self.leaders.setdefault(vertex, 0)
        self.tt = 0
        self.current_leader = 0
        self.count = 0

    def read_graph(handle, reverse=False, f={}):
        lines = fh.read().split('\n')
        graph = {}
        vertices = []
        for l in lines[:]:
            edge_arr = [int(x) for x in l.split(' ')[:-1]]
            if reverse:
                edge_arr = edge_arr[::-1]
            if len(f):
                edge_arr = [f[edge_arr[0]], f[edge_arr[1]]]

            edge = tuple(edge_arr)
            vertex = edge[0]
            graph.setdefault(vertex, [])
            graph[vertex].append(edge)
            vertices.extend(edge_arr)

        return [graph, sorted(list(set(vertices)), reverse=True)]


def DFS_loop(G, firstpass=True):
    for s in G.vertices:
        if not G.explored[s]:
            if not firstpass:
                G.current_leader = s
                G.leaders[s] = s
            DFS(G, s, firstpass)


def DFS(G, s, firstpass):
    G.explored[s] = True
    if s in list(G.graph.keys()):
        for edge in G.graph[s]:
            v = edge[1]

            if not G.explored[v]:
                if not firstpass:
                    G.leaders[v] = G.current_leader
                DFS(G, v, firstpass)
    if firstpass:
        G.tt += 1
        if not G.tt % 1000:
            print(G.tt)
        G.ftime[s] = G.tt

if __name__ == '__main__':
    import sys
    import resource

    sys.setrecursionlimit(10 ** 6)
    resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

    file_name = sys.argv[1]
    fh = open(file_name, 'r')
    rev_graph = dgraph(dgraph.read_graph(fh, reverse=True))
    DFS_loop(rev_graph)

    fh = open(file_name, 'r')
    final_graph = dgraph(dgraph.read_graph(fh, f=rev_graph.ftime))
    DFS_loop(final_graph, firstpass=False)

    print(Counter(final_graph.leaders.values()).most_common(5))

    fh.close()

# Example in the lecture:
# params=[{1:[(1,4)],7:[(7,1)],4:[(4,7)],9:[(9,7),(9,3)],3:[(3,6)],6:[(6,9)],8:[(8,6),(8,5)],5:[(5,2)],2:[(2,8)]},[1,2,3,4,5,6,7,8,9]]
# rev = {}
#
# for _, value in params[0].items():
#     # rev.setdefault(key, [])
#     for item in value:
#         edge = tuple(list(item)[::-1])
#         rev.setdefault(edge[0],[]).append(edge)
#
# newparams = [rev, params[1][::-1]]
# first_graph = dgraph(newparams)
# DFS_loop(first_graph)
# print(first_graph.ftime)
#
# rpl = {}
#
# key_map = first_graph.ftime
# for key, value in params[0].items():
#     mappedkey = key_map[key]
#     rpl.setdefault(mappedkey, [])
#
#     for item in value:
#         rpl[mappedkey].append(tuple(map(lambda x: key_map[x], (item[0], item[1]))))
#
# newparams = [rpl, params[1][::-1]]
# orig_graph = dgraph(newparams)
# DFS_loop(orig_graph, firstpass=False)
# orig_graph.leaders
