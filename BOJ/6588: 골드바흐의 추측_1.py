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
    decimal = [3,5,7,11,13,17,19,23,29,31]
    temp = 0
    while True:
        a = decimal[temp]
        if isPrime(n-a):
            print(f'{n} = {a} + {n-a}')
            break
        else:
            temp += 1