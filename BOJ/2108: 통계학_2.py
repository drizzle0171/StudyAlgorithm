# N: 홀수

import sys
from collections import Counter

N = int(sys.stdin.readline())

N_list = [int(sys.stdin.readline()) for _ in range(N)]

# 평균값
avg = round(sum(N_list)/N)
print(avg)

# 중앙값: 정렬
N_list.sort()
print(N_list[N//2])

# 최빈값
cnt = Counter(N_list).most_common(2)

if len(N_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(cnt)

# 범위
print(N_list[-1]-N_list[0])