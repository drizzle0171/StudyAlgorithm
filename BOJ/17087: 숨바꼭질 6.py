import sys

N, S = map(int, sys.stdin.readline().strip().split())
D = list(map(int, sys.stdin.readline().strip().split()))
distance = []

for i in D:
    distance.append(abs(S-i))

print(min(distance))