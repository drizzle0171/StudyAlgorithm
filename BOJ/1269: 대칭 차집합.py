import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

alist = set(map(int, input().rstrip().split()))
blist = set(map(int, input().rstrip().split()))

ab = alist-blist
ba = blist-alist

print(len(ab) + len(ba))