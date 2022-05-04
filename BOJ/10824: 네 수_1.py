import sys 

A, B, C, D = map(str, sys.stdin.readline().strip().split())
AB = int(A+B)
CD = int(C+D)
print(AB+CD)