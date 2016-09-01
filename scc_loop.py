from collections import Counter
from collections import deque

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

    def read_graph(fhandle, reverse=False, f={}):
        lines = fhandle.read().split('\n')
        graph = {}
        vertices = []
        for l in lines[:]:
            edge_arr = [int(x) for x in l.strip().split(' ')[:]]
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
        G.count += 1
        if G.count % 200 == 0:
            print('progress! %d\n' % G.count)
        if not G.explored[s]:
            if not firstpass:
                G.current_leader = s
                G.leaders[s] = s

            path, path_length = DFS_iter(G, s, firstpass)

            if firstpass:
                for i, node in enumerate(path):
                    G.ftime[node] += G.tt + i + 1
                G.tt += path_length


def DFS_iter(G, s, firstpass):
    G.explored[s] = True
    stack = deque([s])
    path_length = 0
    path = deque()
    while len(stack):
        v = stack.pop()
        if v not in list(G.graph.keys()): #sink node
            G.explored[v] = True
            if not firstpass:
                G.leaders[v] = G.current_leader
        else:
            for v, w in G.graph[v]:
                if not G.explored[w]:
                    G.explored[w] = True
                    stack.append(w)
                    if not firstpass:
                        G.leaders[w] = G.current_leader
        if firstpass:
            path_length += 1
            path.appendleft(v)
        G.count += 1

    return path, path_length



if __name__ == '__main__':
    import sys
    file_name = sys.argv[1]
    file_name = 'SCC.txt'
    fh = open(file_name, 'r')
    rev_graph = dgraph(dgraph.read_graph(fh, reverse=True))

    print('running first loop')
    DFS_loop(rev_graph)

    fh = open(file_name, 'r')
    final_graph = dgraph(dgraph.read_graph(fh, f=rev_graph.ftime))
    print('running second loop')
    DFS_loop(final_graph, firstpass=False)

    print(Counter(final_graph.leaders.values()).most_common(5))

    fh.close()

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
