# N개의 수가 주어졌을 때, 오름차순으로 정렬하는 프로그램

import sys

N = int(sys.stdin.readline())

N_list = []

for i in range(N):
    N_list.append(int(sys.stdin.readline()))
    #for문 속에서 append를 쓰게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용하지 못함

# 버블 정렬 사용해보기

for i in range(N):
    for j in range(N):
        if N_list[i] < N_list[j]:
            N_list[i], N_list[j] = N_list[j], N_list[i]

for k in N_list:
    print(k)