N, M = 0, 0
Max = 0

nine = []
for _ in range(9):
    nine.append(list(map(int, input().split())))

for i in range(9):
    if Max <= max(nine[i]):
        Max = max(nine[i])
        N = i + 1
        M = nine[i].index(max(nine[i])) + 1

print(Max)
print(f"{N} {M}")

# 새로운 곳이 max일 경우 그곳의 인덱스 출력