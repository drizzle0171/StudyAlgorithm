import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
remote = {str(x) for x in range(10)}

if m != 0:
    remote -= set(input().split())

min_cnt = abs(100-n)

for k in range(1000001):
    num = str(k)
    print(num)
    for i in range(len(num)):
        if num[i] not in remote:
            break
        if i == len(num)-1:
            min_cnt = min(min_cnt, abs(n-k)+len(num))

print(min_cnt)