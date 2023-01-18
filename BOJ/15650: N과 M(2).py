import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if (i not in s):
                if len(s) == 0:
                    s.append(i)
                    dfs()
                    s.pop()
                else:
                    for k in range(len(s)-1, len(s)):
                        if s[k] < i:
                            s.append(i)
                            dfs()
                            s.pop()
dfs()