import sys

N = int(sys.stdin.readline())
seq = [int(sys.stdin.readline().strip()) for _ in range(N)]

for i in range(1, len(seq)):
    err = seq[i-1]+1
    if err == seq[i]:
        print('NO')
        break


