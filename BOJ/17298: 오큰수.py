import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
stack = []
answer = [-1]*len(A)

for i, a in enumerate(A):
    while stack and a > A[stack[-1]]:
        index = stack.pop()
        answer[index] = A[i]
    stack.append(i)

for i in answer:
    print(i, end=" ")
