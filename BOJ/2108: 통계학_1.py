# N: 홀수

import sys

N = int(sys.stdin.readline())

N_list = [int(sys.stdin.readline()) for _ in range(N)]

# 평균값
avg = sum(N_list)/N
print(int(avg))

# 중앙값: 정렬
ordered_list = sorted(N_list)
print(ordered_list[N//2])

# 최빈값
count = []
for i in range(N):
    count.append(N_list.count(i))
max = count.index(max(count))
print(N_list[max])

# 범위
print(ordered_list[-1]-ordered_list[0])