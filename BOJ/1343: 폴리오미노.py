import sys
input = sys.stdin.readline

s = input().rstrip()
result = ''
cnt = 0

for i in range(len(s)-1):
    if s[i] == 'X':
        cnt += 1
    if cnt == 2:
        if s[i+1] != 'X':
            result += 'BB'
            cnt = 0
    if cnt == 4:
        result += 'AAAA'
        cnt = 0
    if s[i] == '.':
        result += '.'
        cnt = 0

    
if s[-1] == 'X':
    cnt += 1

if cnt == 2:
    result += 'BB'

if cnt == 4:
    result += 'AAAA'

if len(result) != len(s):
    print(-1)
else:
    print(result)
    

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)