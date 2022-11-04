Nlist = []
for _ in range(5):
    Nlist.append(int(input()))

Nlist = sorted(Nlist)
# mean
print(int(sum(Nlist)/len(Nlist)))

# middle
print(Nlist[int(len(Nlist)/2)])

# 평균은... int 처리 해야 맞음...