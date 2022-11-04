white = list(map(int, input().split()))
normal = [1, 1, 2, 2, 2, 8]

for i in range(len(normal)):
    normal[i] = str(normal[i] - white[i])

print(" ".join(normal))