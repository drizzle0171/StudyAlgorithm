N, M = map(int, input().split())

first = []
for _ in range(N):
    first.append(list(map(int, input().split())))

second = []
for _ in range(N):
    second.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        first[i][j] += second[i][j]
        first[i][j] = str(first[i][j])
    print(" ".join(first[i]))