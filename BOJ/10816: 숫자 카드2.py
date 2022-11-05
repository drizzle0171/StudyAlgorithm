import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nlist = list(map(int, input().rstrip().split()))
counter = Counter(nlist)

M = int(input())
mlist = list(map(int, input().rstrip().split()))

result = ""
for i in range(M):
    result += str(counter[mlist[i]]) + " "

print(result)