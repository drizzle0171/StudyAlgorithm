import sys
input = sys.stdin.readline

s = input()
check = False
cnt = 0

for i in range(len(s)-2):
    if s[i] != s[i+1] and not check:
        cnt += 1
        check = True
    elif s[i] != s[i+1] and check:
        check = False
print(cnt)