N = int(input())
Nlist = list(map(int, input().split()))
Nlist = list(set(Nlist))
Nlist.sort()
for i in Nlist:
    print(i, end=' ')