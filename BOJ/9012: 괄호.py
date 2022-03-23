import sys


import sys

N = int(sys.stdin.readline())
right = '('
left = ')'
for _ in range(N):
    input = sys.stdin.readline().strip()
    right_cnt = input.count(right)
    left_cnt = input.count(left)
    if right_cnt != left_cnt:
        print('NO')
    else:
        print('YES')