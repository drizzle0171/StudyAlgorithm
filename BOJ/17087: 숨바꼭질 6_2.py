import math 
import sys

N, S = map(int, sys.stdin.readline().strip().split())
D = list(map(int, sys.stdin.readline().strip().split()))

distance = []
for i in D:
    distance.append(abs(S-i))

answer = distance[0]
for i in range(len(distance)):
    answer = math.gcd(distance[i], answer)

print(answer)