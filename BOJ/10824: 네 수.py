import sys 

A, B, C, D = map(str, sys.stdin.readline().strip().split())
AB = A+B
CD = C+D
sum = int(AB) + int(CD)
print(sum)