import sys

A, B = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline())
m_list = list(map(str, sys.stdin.readline().strip().split()))
B_list = []

print(m_list)

for i in m_list:
    B_list.append(int(str(int(i, A)), B))

print(B_list)

for i in B_list:
    print(i, end=" ")