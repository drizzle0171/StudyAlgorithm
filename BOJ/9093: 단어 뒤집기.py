import sys

N = int(sys.stdin.readline())

for _ in range(N):
    sentence = sys.stdin.readline().strip().split()
    for i in range(len(sentence)):
        for j in reversed(range(len(sentence[i]))):
            print(sentence[i][j], end="")
        print(end=' ')