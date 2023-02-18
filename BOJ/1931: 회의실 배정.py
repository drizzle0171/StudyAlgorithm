import sys
input = sys.stdin.readline

n = int(input())
meet = []
for _ in range(n):
    meet.append(list(map(int, input().split())))

if n == 1:
    print(1)
else:
    meet.sort(key=lambda x: x[0])
    if meet[0][1] >= meet[1][1]:
        now = meet[1][1]
    else:
        now = meet[0][1]
    cnt = 1


    for i in range(1, n-1):
        if now <= meet[i][0]:
            if meet[i][0] == meet[i+1][0]:
                now = min(meet[i][1], meet[i+1][1])
                cnt += 1
            else:
                now = meet[i][1]
                cnt += 1

    if meet[-1][0] >= now:
        cnt += 1

    print(cnt)

# n = int(input())
# s = []
# for i in range(n):
#     first, second = map(int, input().split())
#     s.append([first, second])
# s = sorted(s, key=lambda a: a[0])
# s = sorted(s, key=lambda a: a[1])
# last = 0
# cnt = 0
# for i, j in s:
#     if i >= last:
#         cnt += 1
#         last = j
# print(cnt)

