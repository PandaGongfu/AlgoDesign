import knapsack
import sys
sys.setrecursionlimit(20000)

def find_vs(n, w, vals, wts, cache):
    if (n, w) not in cache:
        if n == -1 or w == 0:
            cache[(n, w)] = 0
        elif w > wts[n]:
            cache[(n, w)] = max(find_vs(n-1, w, vals, wts, cache), vals[n] + find_vs(n-1, w-wts[n], vals, wts, cache))
        else:
            cache[(n, w)] = find_vs(n-1, w, vals, wts, cache)
    return cache[(n, w)]


values, weights, sacksize = knapsack.read_input('knapsack_big.txt')
cache = {}
print(find_vs(len(values)-1, sacksize, values, weights, cache))
