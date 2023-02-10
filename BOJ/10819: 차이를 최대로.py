import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

maxSum = -801
for comb in permutations(a, n):
    sum = 0
    for i in (range(1, len(range(n)))):
        sum += abs(comb[i-1] - comb[i])
    maxSum = max(sum, maxSum)

print(maxSum) 
