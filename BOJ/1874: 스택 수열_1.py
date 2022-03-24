import sys

N = int(sys.stdin.readline())
s = []
op = []
count = 1
temp = True

for i in range(N):
    num = int(sys.stdin.readline().strip())
    while count <= num: 
        s.append(count) 
        op.append('+')
        count+=1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
    print(f'num: {num}, count: {count}, s: {s}, op: {op}, temp: {temp}')

for i in range(1, len(s)):
    err = s[i-1]+1
    if err == s[i]:
        print('NO')
        break

for i in op:
    print(i)