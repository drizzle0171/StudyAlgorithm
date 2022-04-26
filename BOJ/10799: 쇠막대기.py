laser = list(input())
answer = 0
stack = []

for i in range(len(laser)):
    if laser[i] == '(':
        stack.append('(')

    else:
        if laser[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)

# 출력 초과 나면 input으로 바꾸자...! sys가 언제나 답은 아니구나.