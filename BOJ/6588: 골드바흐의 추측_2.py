import sys
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    TF = [False, False] + [True]*(n-1)
    decimal = []
    for i in range(2, n+1):
        if TF[i]:
            decimal.append(i)
            for j in range(2*i, n+1, i):
                TF[j] = False
    temp = 0
    while True:
        a = decimal[temp]
        if isPrime(n-a):
            print(f'{n} = {a} + {n-a}')
            break
        else:
            temp += 1