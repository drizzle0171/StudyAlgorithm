import sys
input = sys.stdin.readline

n = int(input())

def fib_recusion(n):
    global cnt_re
    cnt_re += 1
    if (n == 1) or (n == 2):
        cnt_re -= 1
        return 1   
    else:
        return fib_recusion(n-1) + fib_recusion(n-2)

def fib_dp(n, cnt_dp):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt_dp += 1
    return dp[n], cnt_dp

cnt_re = 0
result_r = fib_recusion(n)
result_d, cntd = fib_dp(n, 0)

print(cnt_re+1, cntd)