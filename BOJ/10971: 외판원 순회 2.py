import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
w = []
for _ in range(n):
    w.append(list(map(int, input().split())))

minCost = sys.maxsize
for comb in permutations(range(n), n):
    cost = 0
    for i in range(0, len(comb)):
        if w[comb[i-1]][comb[i]] == 0:
            break
        else:
            cost += w[comb[i-1]][comb[i]]
    minCost = min(minCost, cost)
print(minCost)