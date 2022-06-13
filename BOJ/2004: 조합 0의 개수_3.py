import sys
n, m = map(int, sys.stdin.readline().split())
def count(i, j):
    cnt = 0
    while i != 0:
        i//= j
        cnt += i
    return cnt

five = count(n, 5) - count(m, 5) - count((n-m), 5)
two = count(n, 2) - count(m, 2) - count((n-m), 2)

if five < two:
    print(five)
else:
    print(two)
