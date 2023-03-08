# import sys
# import heapq
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     nlist = list(map(int, input().split()))
#     heapq.heapify(nlist)
    
#     if len(nlist)%2 != 0:
#         print(abs(nlist[(n-1)//2]-nlist[-1]))
#     else:
#         back = nlist[n//2-1]
#         forth = nlist[n//2]
#         print(min(abs(back-nlist[-1]), abs(forth-nlist[-1])))

from sys import stdin

for i in range(int(stdin.readline())):
    X = int(stdin.readline())
    nums = sorted(list(map(int, stdin.readline().split())))
    level = 0
    for j in range(2, X):
        level = max(level, abs(nums[j] - nums[j - 2]))
    print(level)