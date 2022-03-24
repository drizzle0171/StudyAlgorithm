import sys

N = int(sys.stdin.readline()) # length of sequence
s = [] # sequence 
op = [] # operator
count = 1 # 1~n의 수열의 시작은 1
temp = True

for i in range(N):
    num = int(sys.stdin.readline().strip()) # 숫자 하나씩 입력 받음
    while count <= num: 
        s.append(count) # sequence에 추가
        op.append('+') # push 연산
        count+=1 # count에 1 추가
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
    print(f'num: {num}, count: {count}, s: {s}, op: {op}, temp: {temp}')

if temp == False:
    print('NO')
else:
    for i in op:
        print(i)