import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

nlist = set()
for _ in range(n):
    nlist.add(input().rstrip())

mlist = set()
for _ in range(m):
    mlist.add(input().rstrip())

result = sorted(list(nlist&mlist))

print(len(result))
for i in result:
    print(i)