# N개의 수가 주어졌을 때, 오름차순으로 정렬하는 프로그램

import sys

N = int(sys.stdin.readline())
N_list = [0]*10001

for i in range(N):
    N_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if N_list[i] != 0:
        for j in range(N_list[i]):
            print(i)

    # if N_list[i] != 0:
    #     print(i) 이렇게 하면 중복 문제를 못 품 !
