import sys

n = int(sys.stdin.readline())

num = []
for _ in range(n):
    num.append(sys.stdin.readline().split())

num.sort(key = lambda x: x[0])

for i in range(1,n):
    for j in range(2, n):
        if num[i-1][0] == num[j][0]:
            if num[i-1][1] > num[j][1]:
                new = num[i-1][1]
                num[i-1][1] = num[j][1]
                num[j][1] = new            

for i in range(n):
    print(" ".join(num[i]))