import sys

T = int(sys.stdin.readline())
cnt = 0

decimal = [True for _ in range(1000001)]

for i in range(2, 1000001):
    if decimal[i]:
        for k in range(i+i, 1000001, i):
            decimal[k] = False
decimal[0], decimal[1] = False, False

while T != cnt:
    answer = 0
    num = int(sys.stdin.readline())
    if num == (2):
        print(0)
    else:
        for i in range(2, int(num/2)+1):
            if decimal[i] and decimal[num-i]:
                answer += 1
        print(answer)
    cnt += 1