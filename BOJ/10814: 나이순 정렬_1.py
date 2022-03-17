import sys

N = int(sys.stdin.readline())

member = []
for i in range(N):
    member.append(list(map(str, sys.stdin.readline().strip().split()))+[i])

member.sort(key = lambda x: (int(x[0]), x[2]))

for i in range(N):
    print(member[i][0], member[i][1])