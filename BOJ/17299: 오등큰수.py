import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
FA = []
answer = [-1]*len(A)
stack = []
cnt = 0

# FA 완성
for i in A:
    for j in A:
        if i == j:
            cnt += 1
    FA.append(cnt)
    cnt = 0
print(FA)


# 오큰수 process at FA
for index, current in enumerate(FA):
    while stack and current > FA[stack[-1]]:
        last = stack.pop()
        answer[last] = A[index]
    stack.append(index)

for i in answer:
    print(i, end=" ")