import sys
input = sys.stdin.readline

n = input()
f = int(input())

m = int(n[:-3]+'00')
i = 0

while(True):
    if (m+i)%f == 0:
        break
    else:
        i += 1
        
print(str(m+i)[-2:])