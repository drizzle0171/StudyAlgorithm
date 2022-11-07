N = int(input())
Nlist = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in Nlist:
    if i == v:
        cnt += 1

print(cnt)