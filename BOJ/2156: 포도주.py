import sys
input = sys.stdin.readline

n = int(input())
nlist = [0]
for n in range(n):
    nlist.append(int(input()))

dp = [0] *(n+1)
dp[1] = nlist[1]
dp[2] = nlist[1]+nlist[2]
three = False

for i in range(3, n+1):
    if i%3 == 0:
        if (nlist[i-1] + nlist[i]) > (dp[i-2] + nlist[i]):
            dp[i] = (nlist[i-1] + nlist[i])
            three = True
        else:
            dp[i] = dp[i-2] + nlist[i]

    else:
        if three == False:
            if (dp[i-2] + nlist[i]) > (dp[i-1] + nlist[i]):
                dp[i] = dp[i-2] + nlist[i]
            else:
                dp[i] = dp[i-1] + nlist[i]
                
        else:
            dp[i] = max((nlist[i-1] + nlist[i]), dp[i-2] + nlist[i])
            three = False

print(max(dp))


# ------------------------------------------------------------------------

n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0]
dp.append(w[1])
if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
print(dp[n])
