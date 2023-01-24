# 틀린 내 풀이
import sys
input = sys.stdin.readline

n = int(input())
building = list(map(int, input().split()))
result = []
for i in range(n-1, 0, -1):
    for j in range(i-1, 0, -1):
        if building[j] > building[i]:
            result.append(j+1)
            break
    if len(building[i:]) != len(result):
        result.append(0)
result.append(0)

for i in range(n-1, -1, -1):
    print(result[i], end=" ")

# 방법 1
import sys
input = sys.stdin.readline

n = int(input())
t_list = list(map(int, input().split()))
result = []
stack = []

for i in range(n):
    current = t_list[i]
    if stack:
        while stack:
            if stack[-1][0] < current:
                stack.pop()
                if not stack:
                    print(0, end=" ")
            elif stack[-1][0] > current:
                print(stack[-1][1]+1, end=" ")
                break
            else:
                print(stack[-1][1]+1, end=" ")
                break
        stack.append([current, i])
    else:
        print(0, end=" ")
        stack.append([current, i])

# 방법 2
import sys
n = int(sys.stdin.readline())
t_list = list(map(int, sys.stdin.readline().split()))
stack = []
goto = [0]*n

for i in range(n):
    current = t_list[i]
    while stack and t_list[stack[-1]]<current:
        stack.pop()
    if stack:
        goto[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, goto))))