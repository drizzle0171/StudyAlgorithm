import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
for _ in range(q):
    alpha, m, n = map(str, input().rstrip().split())
    m = int(m)
    n = int(n)
    
    alpha_list = []
    temp = 0
    for i in s:
        if i == alpha:
            temp += 1
        alpha_list.append(temp)
    if m != 0:
        print(alpha_list[n]-alpha_list[m-1])
    else:
        print(alpha_list[n]-alpha_list[m])
        
import sys

input = sys.stdin.readline

name = input().strip()
n = int(input())
arr = [[0 for i in range(26)] for i in range(len(name))]
arr[0][ord(name[0]) - 97] = 1
for i in range(1, len(name)):
    arr[i][ord(name[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]
for i in range(n):
    a = input().split()
    if int(a[1]) > 0:
        res = arr[int(
            a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97]
    else:
        res = arr[int(a[2])][ord(a[0]) - 97]
    print(res)