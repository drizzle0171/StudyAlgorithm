import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = roads[0] * costs [0]
minimum = costs[0]

dist = 0

for i in range(1, n-1):
    if costs[i] < minimum:
        res += minimum * dist
        dist = roads[i]
        minimum = costs[i]
    else:
        dist += roads[i]
    
    if i == n-2:
        res += minimum * dist
        
print(res)