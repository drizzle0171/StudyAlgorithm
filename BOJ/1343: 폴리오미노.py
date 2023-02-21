import sys
input = sys.stdin.readline

s = input().rstrip()
result = ''
cnt = 0

for i in range(len(s)):
    print(cnt, s[i], result)
    if s[i] == 'X':
        cnt += 1
        if cnt == 4:
            result += 'AAAA'
            cnt = 0
        elif cnt == 2:
            result += 'BB'
            cnt = 0
    if s[i] == '.':
        if cnt == 4:
            result += 'AAAA'
            cnt = 0
        elif cnt == 2:
            result += 'BB'
            cnt = 0

if len(result) == 0:
    print(-1)
else:
    print(result)