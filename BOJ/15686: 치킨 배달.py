import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = []
distance = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    city.append(list(map(int, input().split())))

chickens =  []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickens.append([i, j])

all_distance = []
for comb in combinations(chickens, m):
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                temp = 0
                minDistance = (n-1)*2
                for chicken in comb:
                    temp = abs(i-chicken[0]) + abs(j-chicken[1])
                    minDistance = min(temp, minDistance)
                    distance[i][j] = minDistance
    total = 0
    for i in range(n):
        total += sum(distance[i])
    all_distance.append(total)


print(min(all_distance))