import sys

test = int(sys.stdin.readline())
cnt = 0

while cnt!=test:
    gcd = list()
    num = list(map(int, sys.stdin.readline().strip().split()))
    num.remove(num[0])
    for a in range(len(num)):
        for b in range(a+1, len(num)):
            i = num[a]
            j = num[b]
            while True:
                print(i, j)
                r = i%j
                if r == 0:
                    gcd.append(j)
                    break
                else:
                    i = j
                    j = r
    print(sum(gcd))
    cnt += 1

def gcd(x, y):
    while(y):
        x, y = y, x%y
        return x