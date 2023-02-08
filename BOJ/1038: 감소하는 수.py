# import sys
# input = sys.stdin.readline

# n = int(input())
# i = 0
# answer = ''

# while True:
#     if len(str(n))==1:
#         print(n)
#         break
    
#     if i == n:
#         print(answer)
#         break
    
#     num = sorted(list(str(i)), reverse=True)
#     for j in range(len(num)-1):
#         if int(num[j]) < int(num[j+1]):
#             break
#         else:
#             answer += num[j]
#     i += 1
        
import sys
input = sys.stdin.readline

n = int(input())
digit = 1
num = []
decrease = []

def dfs(k):
    if len(num) == digit:
        decrease.append(int("".join(map(str, num))))
        return
    for i in range(k, -1, -1):
        if i not in num:
            num.append(i)
            dfs(i-1)
            num.pop()

while len(decrease) <= n:
    dfs(9)
    digit += 1
    if digit == 11:
        print(-1)
        exit()

decrease = sorted(decrease)
print(decrease[n])