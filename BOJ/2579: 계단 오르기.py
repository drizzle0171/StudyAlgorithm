import sys
input = sys.stdin.readline

n = int(input())
nlist = [int(input()) for i in range(n)]
nlist.reverse() # 바꿔서 하는 게 편함

dp = [0]*n
dp[0] = nlist[0]
if len(nlist) > 1:
    dp[1] = dp[0] + nlist[1]

if len(nlist) > 2:
    dp[2] = dp[0] + nlist[2]

for i in range(3, n):
    dp[i] = max((dp[i-3] + nlist[i-1] + nlist[i]), (dp[i-4]+nlist[i-2]+nlist[i]), (dp[i-2]+nlist[i]))

print(max(dp[n-2:]))