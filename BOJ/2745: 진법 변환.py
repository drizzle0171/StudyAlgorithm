import sys

N, B = map(str, sys.stdin.readline().strip().split())
B = int(B)
answer = 0
toAlpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if N[0].isalpha():
    quotient = toAlpha.index(N[0])
else:
    quotient = int(N[0])

for i in N[1:]:
    if i.isalpha():
        remainder = toAlpha.index(i)
    else:
        remainder = int(i)
    answer = quotient * B + remainder
    quotient = answer
    
print(answer)
