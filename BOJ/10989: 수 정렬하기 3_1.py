# N개의 수가 주어졌을 때, 오름차순으로 정렬하는 프로그램

import sys

N = int(sys.stdin.readline())

N_list = []

for i in range(N):
    N_list.append(int(sys.stdin.readline()))

# 버블 정렬 사용해보기

for i in range(N):
    for j in range(N):
        if N_list[i] < N_list[j]:
            N_list[i], N_list[j] = N_list[j], N_list[i]

for k in N_list:
    print(k)