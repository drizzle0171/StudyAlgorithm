import sys
input = sys.stdin.readline

n = list(input().rstrip())
n.sort(reverse=True)
n = int("".join(n))

if n%30==0:
    print(n)
else:
    print(-1)