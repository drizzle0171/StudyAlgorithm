import sys
input = sys.stdin.readline

n = int(input())
maximum = 1003003
che = [False, False] + [True]*(maximum)

def palindrome(answer):
    for k in range(len(answer)//2):
        if answer[k] != answer[len(answer)-k-1]:
            return False
    return True

primes = []

for i in range(2, maximum):
    if che[i]:
        if i >= n:
            primes.append(i)
        for j in range(2*i, maximum, i):
            che[j] = False        

for i in primes:
    if palindrome(str(i)):
        print(i)
        exit()
        