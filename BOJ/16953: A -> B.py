import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 0

while a != b:
    if a > b:
        print(-1)
        exit()
    if str(int(b))[-1] == '1':
        cnt += 1
        b = str(int(b))
        len_b = len(b)
        b = int(b[:(len_b-1)])
    else:
        if b%2 != 0:
            print(-1)
            exit()
        cnt += 1
        b = b/2


print(cnt+1)