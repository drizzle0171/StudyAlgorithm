import sys
input = sys.stdin.readline

n, m = map(int, input().split())
six = []
one = []

for _ in range(m):
    Set, Single = map(int, input().split())
    six.append(Set)
    one.append(Single)    

six.sort()
one.sort()
total = 0

while n!=0:
    if n >=6:
        total += six[0]                
        n -=6
    else:
        total = min(total+six[0], total+(one[0]*n))
        n = 0
        
print(total)