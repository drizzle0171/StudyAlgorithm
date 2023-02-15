# import sys 
# from itertools import permutations
# input = sys.stdin.readline

# n = int(input())
# people = list(map(int, input().split()))

# minSum = float('inf')
# Sum = 0
# cantidate = [0] * 5
# for perm in permutations(people, 5):
#     for i in range(len(perm)):
#         cantidate[i] = perm[i] + sum(perm[:i])
#     Sum = sum(cantidate)
#     minSum = min(Sum, minSum)

# print(minSum)

import sys
input = sys.stdin.readline

n = int(input())
people = sorted(list(map(int, input().split())))
Sum = 0
for i in range(n):
    for j in range(i+1):
        Sum += people[j]
print(Sum)

