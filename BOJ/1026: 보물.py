import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

A.sort()
B.sort(reverse=True)

sum=0
for i, j in zip(A, B):
    sum+= i*j

print(sum)