import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nlist = list(map(int, input().split()))
presum = [0]

temp = 0
for i in nlist:
    temp += i
    presum.append(temp)

maxSum = -100*n-1
for i in range(10-(k-1)):
    Sum = presum[i+k]-presum[i]
    maxSum = max(maxSum, Sum)

print(maxSum)