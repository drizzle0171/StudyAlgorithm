import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().rstrip().split()))
dp = [0] * 100000

for i in range(n):
    temp = nlist[:(i+1)]
    temp_sum = []
    for j in range(i+1):
        temp_sum.append(sum(temp[-j:]))
    dp[i] = max(temp_sum)
print(max(dp))       