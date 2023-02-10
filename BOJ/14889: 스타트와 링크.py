import sys
from itertools import combinations, permutations
input = sys.stdin.readline

n = int(input()) # 짝수
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

minTotal = 100*(n**2)
for comb in combinations(range(n), n//2):
    total = 0
    sum_start = 0
    sum_link = 0
    start = list(comb)
    link = [i for i in range(n) if i not in start]
    for pair in permutations(start, 2):
        sum_start += s[pair[0]][pair[1]]
    for pair in permutations(link, 2):
        sum_link += s[pair[0]][pair[1]]
    minTotal = min(minTotal, abs(sum_start-sum_link))

print(minTotal)