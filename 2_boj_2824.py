N = int(input())
N_list = (input().split())
M = int(input())
M_list = (input().split())

A, B = 1, 1

for i in range(N):
    A *= i

for j in range(M):
    B *= j

while (B!=0):
    A, B = B, A%B

print(B)
