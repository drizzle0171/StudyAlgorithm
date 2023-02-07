import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())

if n%2 == 0:
    while n != 0:
        
        n = n//2
    
else:
    for i in range(n, 2, -2):