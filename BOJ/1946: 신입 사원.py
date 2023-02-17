import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    apply = []
    for _ in range(n):
        apply.append(list(map(int, input().split())))

    paper = sorted(apply, key=lambda x: x[0])
    minimum = paper[0][1]
    cnt = 1

    for i in range(1, n):
        temp = minimum
        minimum = min(paper[i][1], minimum)
        if minimum != temp:
            cnt += 1

    print(cnt)