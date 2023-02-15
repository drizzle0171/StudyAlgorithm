import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
cnt = 0

k = str(k)

for i in k:
    i = int(i)
    if i < 5:
        cnt += i 
    elif i == 5:
        cnt += 1
    else:
        cnt += (i-5) + 1

print(cnt)
