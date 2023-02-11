import sys
import math
from itertools import combinations
input = sys.stdin.readline

n = int(input())

maximum = int(math.sqrt(n))
num_list = list(range(1, maximum+1))
num_list = [o**2 for o in num_list]

two = combinations(num_list, 2)
three = combinations(num_list, 3)
four = combinations(num_list, 4)

minCnt = 5
cnt = 0

for o in num_list:
    if o == n:
        cnt = 1
        minCnt = min(cnt, minCnt)
        print(minCnt)
        exit()

for tw in two:
    if sum(tw) == n:
        cnt = 2
        minCnt = min(cnt, minCnt)
        print(minCnt)
        exit()

for th in three:
    if sum(th) == n:
        cnt = 3
        minCnt = min(cnt, minCnt)
        print(minCnt)
        exit()

for f in four:
    if sum(f) == n:
        cnt = 4
        minCnt = min(cnt, minCnt)
        print(minCnt)
        exit()