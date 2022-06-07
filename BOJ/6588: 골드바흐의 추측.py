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
    decimal = []
    for i in range(3, round(n/2)+1):
        if isPrime(i):
            decimal.append(i)
    temp = 0
    while True:
        a = decimal[temp]
        if isPrime(n-a):
            b = n-a
            print(f'{n} = {a} + {b}')
            break
        else:
            temp += 1
            a = decimal[temp]
