import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
num = []

for i in range(1, 101):
    if i**2 >= m and i**2 <= n:
        num.append(i**2)
        
if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(min(num))