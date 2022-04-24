N = int(input())
Nlist = list(map(int, input().split()))
Nlist = list(set(Nlist))
Nlist.sort()
for i in Nlist:
    print(i, end=' ')

# 중복 제거 -> 정렬 순으로 해야 맞음