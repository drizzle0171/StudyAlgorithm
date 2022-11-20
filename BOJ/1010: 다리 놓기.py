import sys
input = sys.stdin.readline

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

t = int(input())

for _ in range(t):
    n, m = map(int, input().rstrip().split())
    print(int(factorial(m)/(factorial(m-n)*factorial(n))))

