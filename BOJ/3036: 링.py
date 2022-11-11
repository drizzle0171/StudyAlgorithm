import sys
input = sys.stdin.readline

N = int(input())
nlist = list(map(int, input().rstrip().split()))
largest = 0

def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x
    
for i in nlist[1:]:
        print(f'{nlist[0]//GCD(nlist[0], i)}/{i//GCD(nlist[0], i)}')
