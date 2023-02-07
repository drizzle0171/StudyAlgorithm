import sys
input = sys.stdin.readline

n = int(input())
factorial = []

def dfs():
    if len(factorial) == n:
        print(" ".join(map(str, factorial)))
        return

    for i in range(1, n+1):
        if i not in factorial:
            factorial.append(i)
            dfs()
            factorial.pop()

dfs()

