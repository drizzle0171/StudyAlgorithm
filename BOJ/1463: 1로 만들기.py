import sys

N = int(sys.stdin.readline())

while N != 1:
    if (N-1)%2==0 or (N-1)%3==0:
        N = N-1
    if N%2 == 0:
        N = N%2
    
    