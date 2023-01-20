import sys
input = sys.stdin.readline

k = int(input())
k_list = list(map(str, input().split()))
num = []
answer = []

def dfs(sign_position, possible_list):
    
    print(num, sign_position)
    if len(num) == (k+1):
        answer.append("".join(map(str, num)))
        return


    for i in possible_list:
        if sign_position > 1:
            sign_position = len(num)-2
        print(sign_position)
        if i not in num:
            if k_list[sign_position] == '<':
                num.append(i)
                dfs(sign_position+1, possible_list[i+1:])
                num.pop()
            else:
                num.append(i)
                dfs(sign_position+1, possible_list[:i-1])
                num.pop()

dfs(0, list(range(9)))

print(max(answer))
print(min(answer))