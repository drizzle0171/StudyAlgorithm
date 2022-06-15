import math 
import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().strip().split())
D = list(map(int, sys.stdin.readline().strip().split()))

distance = []
for i in D:
    distance.append(abs(S-i))

combination = combinations(distance, 2)
GCD = set()
for i in combination:
    GCD.add(math.gcd(i[0], i[1]))

print(min(GCD))