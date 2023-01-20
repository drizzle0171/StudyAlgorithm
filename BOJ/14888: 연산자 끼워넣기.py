import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
operator = list(map(int, input().split()))
answer = []
count = 1
result = a[0]

def dfs(start, operator_list):
    oper = operator_list.copy()
    print(oper, operator_list)
    global result
    global count
    
    if count == len(a):
        print('종료')
        answer.append(result)
        result = 0
        return
    
    for i in range(start, len(a)-1):
        if operator_list[0]:
            print('a')
            result += a[i+1]
            count +=1
            oper[0] -=1
            print(oper, operator_list)
            dfs(i+1, oper)
        if operator_list[1]:
            print('b')
            result -= a[i+1]
            count +=1
            oper[1] -=1
            dfs(i+1, oper)
        if operator_list[2]:
            print('c')
            print(oper, operator_list)
            result *= a[i+1]
            count +=1
            oper[2] -=1
            print(oper, operator_list)
            dfs(i+1, oper)
        if operator_list[3]:
            print('d')
            result = result//a[i+1]
            count +=1
            oper[3] -=1
            dfs(i+1, oper)

dfs(0, operator)
print(answer)


print(max(answer))
print(min(answer))