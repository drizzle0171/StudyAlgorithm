from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = []
    for _ in range(n):
        m, k = map(str, input().rstrip().split())
        clothes.append(k)
    result = Counter(clothes)
    num = 1
    for key in result:
        num *= result[key] + 1
    print(num-1)